# Output artefacts

The scripts write their results to the `outputs/` directory, which is ignored
by git so that the repository stays clean. The artefacts of a full run are:

| File | Produced by | Contents |
| --- | --- | --- |
| `sentiment_summary.csv` | `scripts/sentiment_summary.py` | Reviews per rating and sentiment label. |
| `sentiment_by_score.csv` | `scripts/export_summary.py` | The same table in long format. |
| `sentiment_by_month.csv` | `scripts/export_summary.py` | Monthly sentiment trend over the review period. |

## Notes

- The directory is created automatically when a script runs.
- The files are deterministic for a given dataset, so they can be regenerated
  and compared.
- The numbers recorded in `docs/findings.md` were produced with the committed
  version of the dataset.

## Recreating the tables

```bash
python scripts/sentiment_summary.py
python scripts/export_summary.py
ls outputs
```
