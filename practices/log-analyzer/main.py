"""Parses a log file and print some metrics."""

import json
import sys
import time
from pathlib import Path
from typing import Final

from log_parser import LogMetrics, LogParser, LogRow

LOG_FILEPATH: Final[Path] = Path(__file__).parent.absolute() / "access.log"
METRICS_FILEPATH: Final[Path] = Path("log_output.json")


if __name__ == "__main__":

    print("Log file downloaded from: https://www.secrepo.com/squid/access.log.gz")
    parser: LogParser = LogParser()
    try:
        log_data: dict[int, LogRow] = parser.parse_file(LOG_FILEPATH)
    except FileNotFoundError as err:
        print(f"File not found due to error: {err}.")
        raise sys.exit(1)

    print("Analyzing log data.")
    log_metrics: LogMetrics = LogMetrics(log_data)
    most_frequent_IPs = log_metrics.frequent_ip_addresses("most_common")
    least_frequent_IPs = log_metrics.frequent_ip_addresses("less_common")
    events_per_sec = log_metrics.events_per_second()
    bytes_exchanged = log_metrics.total_bytes()

    print("Saving log data to json file.")
    with open(METRICS_FILEPATH, "w", encoding="utf-8") as f:
        now = time.strftime("%Y-%m-%dT:%H:%M:%S")
        json.dump(
            {
                f"output_{now}": {
                    "most_frequent_IPs": most_frequent_IPs,
                    "least_frequent_IPs": least_frequent_IPs,
                    "events_per_sec": events_per_sec,
                    "bytes_exchanged": bytes_exchanged,
                }
            },
            f,
        )
