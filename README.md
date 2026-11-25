[![Make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/firlifirrizqi/one-line-exit-makefun/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/firlifirrizqi/one-line-exit-makefun/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

# The One-Line Exit

One-line entry for the [Make.fun bounty](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1) of the same name: a resignation letter exactly one line long, whose only job is to be funny.

## The line

> Dear Team, I quit: the office plant I was told to water has outlived three managers, and I am not waiting to see who it takes next.

## How it works

`main.py` writes that single line (131 characters, within the 200-character limit) to `/output/entry.txt`. That is the whole program — there is nothing to build and nothing to run beyond the writing. It then re-reads the file and verifies the output is byte-identical to the chosen line, a single line, and 1–200 characters.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
