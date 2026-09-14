# AI CFO Copilot

An AI assistant that answers finance questions against live company data.

Status: repository scaffold. The implementation is being migrated in — structure, architecture, and interfaces are in place.

Built by [[Jasmine Tabaie]](https://jasminet.lovable.app/)
---



## What it does

- Pulls live external company and market data through Bright Data, so answers are grounded in current filings and disclosures rather than model memory.
- Runs finance-specific analysis through the Anthropic Claude API — variance explanation, revenue trend reading, and anomaly flagging.
- Returns results through a React interface built for a finance user, not a developer.

## Why I built it

I spent seven years closing books and a year auditing federal returns, and the pattern was the same in both seats: the analysis was never the slow part. Gathering the data was. Most of a close or an audit is retrieval — finding the contract, pulling the comparable, reconciling two systems that disagree.

This was an experiment in collapsing that retrieval step. Not a chatbot bolted onto a ledger, but a tool that fetches the underlying data first and reasons over it second, so the output can be traced back to a source a controller would accept.



## Architecture

```
React frontend  →  Python API  →  ┌─ Claude API      (reasoning, explanation)
                                  └─ Bright Data     (live data retrieval)
```

| Layer | Technology |
|---|---|
| Frontend | React |
| Backend | Python |
| Reasoning | Anthropic Claude API |
| Data retrieval | Bright Data |



## Screenshots

<!-- TODO (Jasmine): drop 2–3 screenshots into docs/screenshots/ and link them here.
     This is the single highest-value addition to this README — most people who
     open the repo will look at the images and never read the code. -->

## Running locally

You'll need Python 3.10+, Node 18+, an Anthropic API key, and a Bright Data API key.

```bash
# 1. clone
git clone https://github.com/<your-username>/ai-cfo-copilot.git
cd ai-cfo-copilot

# 2. backend
pip install -r requirements.txt
cp .env.example .env        # then add your keys to .env
python backend/main.py

# 3. frontend (new terminal)
cd frontend
npm install
npm run dev
```

Never commit your `.env` file. It is listed in `.gitignore` for that reason.

## Project structure

```
ai-cfo-copilot/
├── backend/
│   ├── main.py               API entry point
│   ├── claude_client.py      Anthropic Claude API wrapper
│   ├── brightdata_client.py  Bright Data retrieval wrapper
│   └── analysis.py           Finance logic — variance, trend, anomaly
├── frontend/
│   └── src/                  React application
├── docs/screenshots/         Interface screenshots
├── .env.example              Template for required API keys
└── requirements.txt
```

## What I'd build next



- Source citation on every figure returned, so a reviewer can tie each number to its origin document.
- An evaluation set of known-answer finance questions, to measure where the model is wrong rather than assuming it isn't.
- Support for multi-period comparison rather than point-in-time lookup.

## About

I'm a senior revenue accountant working at the intersection of technical accounting and applied AI — ASC revenue recognition, GAAP reporting, and federal audit, plus Python and PyTorch automation for close and reconciliation work.

- Website: (https://jtab8-github-io.vercel.app/)
- LinkedIn: https://www.linkedin.com/in/jt90/

## License

MIT — see [LICENSE](LICENSE).
