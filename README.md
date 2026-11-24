[![competition](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/qienzdork/judge-laugh-developer-excuses/rank.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/qienzdork/judge-laugh-developer-excuses/reward.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

# Make the AI Judge Laugh: Developer Excuses

One funny single-line excuse a developer gives when code breaks in production.

## The entry

> Production broke because my code passed all my tests — and my tests were written by me, the person who wrote the bug.

## How it works

`main.py` writes that single line to `/output/entry.txt` (or `$OUTPUT_PATH` when set, for local validation). No network, no dependencies, no secrets — just the line, deterministic on every run.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
