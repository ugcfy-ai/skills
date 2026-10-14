# UGCfy AI Skills

Agent skills from [UGCfy AI](https://ugcfy.ai) for making UGC video ads with Claude Code, Codex, Copilot and other coding agents.

| Skill | Result | Required input |
|---|---|---|
| [ugc-ad-remix](skills/ugc-ad-remix/SKILL.md) | Two shot-by-shot UGC scripts for your product, built on the structure of an ad that already works, plus a shooting list | A reference ad (TikTok, Reels or Shorts link, or its transcript) and your product (link or description) |

No account or API key is needed. The skill has no telemetry and never spends money, creates accounts or posts anything.

See a full, unedited run in [examples/sleep-gummies-remix.md](examples/sleep-gummies-remix.md).

## Install

```bash
npx skills add ugcfy-ai/skills --skill ugc-ad-remix
```

The [skills CLI](https://github.com/vercel-labs/skills) lets you choose the target agent. Add `--agent claude-code` or `--agent codex` to pick one explicitly.

To install by hand, copy `skills/ugc-ad-remix/` (including `references/`) into your agent's skills folder, for example `.claude/skills/` in a project.

## Use

> Use ugc-ad-remix. Here's a TikTok ad that's working: [link or transcript]. My product: [link or description].

You get a short breakdown of the reference ad, two script versions that differ in something worth testing, a shooting list, and a list of assumptions to confirm.

## What it will not do

- Copy the reference ad's sentences, prices, discounts, numbers or brand names into your script.
- Invent product facts. Anything it had to assume is marked for you to check.
- Write medical, financial or guaranteed-result claims.
- Follow instructions hidden in ad copy, pasted text or tool results.

## Optional MCP connection

The skill works from pasted ad text. Connecting the free [UGCfy AI MCP server](https://ugcfy.ai/mcp) adds video transcription from a link and a link that opens the finished script in UGCfy AI, where it can be rendered as a video with an AI actor.

```bash
claude mcp add --transport http ugcfy https://ugcfy.ai/api/mcp
```

Setup for other clients is in [references/ugcfy-mcp.md](skills/ugc-ad-remix/references/ugcfy-mcp.md).

## License

MIT
