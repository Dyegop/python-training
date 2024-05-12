"""This module contains a parser that loads and parses a logfile from
https://www.secrepo.com/squid/access.log.gz.

The parser is able to return some metrics from the parsed logfile.
"""

from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass
class LogRow:
    """Represents row in a log file."""

    timestamp: float
    header_size: int
    ip_address: str
    response_code: str
    response_size: int
    request_method: str
    url: str
    username: str
    access_destination_type: str
    response_type: str

    def __getitem__(self, item):
        return getattr(self, item)


class LogParser:
    """A class that Parses a log file."""

    def parse_file(
        self, log_filepath: Path, enconding: str = "utf-8", ignore_headers: bool = True
    ) -> dict[int, LogRow]:
        """Parses the given file to the given encoding (utf-8 by default).

        Args:
            log_filepath: The filepath of the log file.
            enconding: The encoding we want to use to parse the lof file.
            ignore_headers: True if we want to ignore the first line of the log file, False
            otherwise.
        Returns:
            A dict with the row number and the parsed row.
        """

        result: dict[int, LogRow] = {}
        row_number: int = 1
        for line in self._read_lines(log_filepath, enconding, ignore_headers):
            try:
                result[row_number] = LogRow(
                    timestamp=float(line[0]),
                    header_size=int(line[1]),
                    ip_address=line[2],
                    response_code=line[3],
                    response_size=int(line[4]),
                    request_method=line[5],
                    url=line[6],
                    username=line[7],
                    access_destination_type=line[8],
                    response_type=line[9],
                )
                row_number += 1
            except ValueError as err:
                print(
                    f"ValueError when parsing line {row_number}: {err}. Skipping line."
                )
            except IndexError as err:
                print(f"IndexError parsing line {row_number}: {err}. Skipping line.")

        return result

    @staticmethod
    def _read_lines(
        log_filepath: Path, enconding: str, ignore_headers: bool
    ) -> list[list[str]]:
        """Read lines in a file and returns them."""

        with open(log_filepath, mode="r", encoding=enconding) as f:
            file_lines: list[str] = (
                f.readlines()[1:] if ignore_headers else f.readlines()
            )
            result: list[list[str]] = [line.split() for line in file_lines]
            print(f"Found a total of {len(result)} lines in file {log_filepath}.")
            return result


class LogMetrics:
    """A class that returns metrisc from a given log file."""

    def __init__(self, log_data: dict[int, LogRow]) -> None:
        self.log_data: dict[int, LogRow] = log_data

    def frequent_ip_addresses(self, frequency: str) -> list[str]:
        """Returns the most/less frequent IP addresses."""

        all_ip_address = [row["ip_address"] for row in self.log_data.values()]
        counter = Counter(all_ip_address).most_common()

        freq_condition: int
        if frequency == "most_common":
            freq_condition = max(ip[1] for ip in counter)
        elif frequency == "less_common":
            freq_condition = min(ip[1] for ip in counter)
        else:
            print(f"Incorrect value selected for frequency: {frequency}.")
            raise ValueError

        result: list[str] = [ip[0] for ip in counter if ip[1] == freq_condition]
        return result

    def events_per_second(self) -> float:
        """Returns the number of events per second that are logged."""

        max_timestamp = max(row["timestamp"] for row in self.log_data.values())
        min_timestamp = min(row["timestamp"] for row in self.log_data.values())
        total_time = max_timestamp - min_timestamp
        total_events = len(self.log_data)
        return total_events / total_time

    def total_bytes(self) -> int:
        """Returns the total amount of bytes exchanged (response + response header)."""

        total_header_size = sum(row["header_size"] for row in self.log_data.values())
        total_response_size = sum(
            row["response_size"] for row in self.log_data.values()
        )
        return total_header_size + total_response_size
