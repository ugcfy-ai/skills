# Example: remixing a skincare UGC ad for sleep gummies

Both the reference ad and the product are synthetic. "Drift" is not a real brand. This is the unedited output of the `ugc-ad-remix` skill in Claude Code, without the UGCfy AI MCP connected, from this prompt:

> Use the ugc-ad-remix skill.
>
> Reference ad (TikTok, transcript I copied): "Okay I need to talk about this because nobody told me. I have had dark circles since high school. I tried every concealer, every eye cream, nothing. My friend sent me this caffeine eye serum and I was like sure, whatever. Two weeks later, look at this. No filter. This is my real under eye. It is like eleven dollars and it lasts me two months. They are doing buy one get one right now so honestly just go get it, link is in my bio."
>
> My product: Drift magnesium glycinate sleep gummies. 30 gummies per jar, $24. Non-habit forming. For adults who wake up at 3am and cannot fall back asleep. Mixed berry flavor.

Note what it left behind: the serum's $11 price, the two-month claim, the buy-one-get-one offer and the "two weeks" result. Every product fact in the scripts comes from the product description.

---

No UGCfy AI MCP is connected here, so I worked from the transcript you pasted. You can connect it for free at `https://ugcfy.ai/api/mcp`, though you don't need it for this.

## 1. Reference breakdown

- **Hook (curiosity):** "Okay I need to talk about this because nobody told me." It suggests the viewer is missing out on something, and the speaker sounds like a friend passing on a tip, not a brand.
- **Structure:** hook → problem (a long-running issue, everything already tried) → discovery (a friend's recommendation, met with doubt) → proof ("two weeks later, look at this") → offer (price, how long it lasts, BOGO) → cta (link in bio)
- **What I borrowed:**
  1. Say how long the problem has gone on and that the usual fixes didn't work.
  2. Admit you doubted it before getting to the result.
  3. Treat the price as a shrug ("it's like…"), not a pitch.
- **What I left out:** the $11 price, "lasts two months", the BOGO deal, "two weeks", "no filter", and every claim the serum ad makes.

## 2. Version A: Curiosity hook, talking to camera (closest to the reference)

| # | Time | Visual | Camera | Voiceover | On-screen text |
|---|---|---|---|---|---|
| 1 | 0–3s | Creator in bed, hair messy, leans close to the lens as if sharing a secret | Selfie, handheld, close-up | "Okay, why did nobody tell me about this." | Nobody told me this 😩 |
| 2 | 3–9s | Dark bedroom, phone lights up a face. Cut to the phone lock screen showing 3:00-something | Selfie, then an insert of the phone | "I wake up at 3am. Every night. And then I'm just… up. I've tried no screens, no coffee, all of it." | The 3am wake-up club |
| 3 | 9–14s | Creator on the couch, holds up the Drift jar, makes a doubtful face | Medium shot, phone on a stand | "My friend gave me these magnesium glycinate gummies and I was like, a gummy? Sure." | A gummy?? ok sure |
| 4 | 14–21s | Morning light. Creator opens the curtains, then sits on the edge of the bed with coffee and looks calmly at the camera | Selfie, natural light | "Then I'm opening my eyes and it's actually morning. I'm not going to say it fixes everything. I'm just saying I noticed." | Woke up to actual daylight |
| 5 | 21–27s | Shakes the jar, eats a gummy on camera, small nod | Close-up on hand and jar, then face | "They're mixed berry, they're not habit forming, and it's twenty-four bucks for a jar of thirty. Link's in my bio." | Mixed berry · non-habit forming · link in bio |

**Total:** about 27 seconds · **Borrowed from the reference:** the "nobody told me" curiosity hook, the friend tip met with doubt, and the casual price line at the end.

## 3. Version B: Problem hook, voiceover over b-roll

This tests whether naming the exact 3am moment stops the scroll better than a curiosity line. It also needs no face on camera.

| # | Time | Visual | Camera | Voiceover | On-screen text |
|---|---|---|---|---|---|
| 1 | 0–3s | Bedside clock or phone in the dark, reading 3-something AM | Static close-up, low light | "If you wake up at 3am and just can't get back to sleep…" | 3am. Wide awake. Again. |
| 2 | 3–9s | Ceiling, then a hand reaching for the phone, then scrolling in the dark | Overhead, then over the shoulder | "…and you've already tried every sleep hack on this app, same." | Tried every sleep hack |
| 3 | 9–15s | The Drift jar on a nightstand next to a book and a glass of water; a hand opens it | Slow push-in, warm lamp light | "Someone told me to try magnesium glycinate, so I got these. I didn't expect much." | Didn't expect much |
| 4 | 15–21s | Blinds open to morning light, the bed is a mess, the alarm gets switched off | Static wide shot, then close-up on the alarm | "This is the part I care about: waking up to my alarm, not the dark." | Alarm > 3am |
| 5 | 21–26s | Hand puts a gummy in their mouth, jar label turned to face the camera | Close-up | "Mixed berry, non-habit forming, thirty in a jar. Link's in my bio." | Drift · link in bio |

**Total:** about 26 seconds · **Borrowed from the reference:** the long-running problem with the usual fixes failing, a doubtful discovery, and an understated close.

## 4. Shooting list

- **People:**
  - Version A: one adult creator on camera.
  - Version B: voiceover only, plus hands.
- **Props:** a Drift jar with the label readable, a phone or bedside clock, a mug, a book, a glass of water, a lamp.
- **Locations:**
  - Bedroom at night, kept dark (the 3am shots).
  - Bedroom in the morning with daylight.
  - A couch or kitchen for Version A shot 3.
- **Things to confirm:**
  - `[assumed: 1 gummy per serving]`: the scripts show one gummy being eaten. If a serving is 2 gummies, change shot 5. Don't say how long a jar lasts until the serving size is confirmed.
  - `[assumed: no current offer]`: both versions end with "link in bio" only. If you are running a promo, add it to the last shot.
  - **Compliance:** this is a supplement, so the scripts never say it treats insomnia or that it "makes you sleep through the night". They only describe what the creator noticed. Check what wording your brand is allowed to use (structure/function claims) and whether you need the FDA disclaimer on screen.
  - **Worth capturing for real:** if a creator has actual sleep-tracker screenshots from before and after, you could use one in the proof shot. Use only real data, never mocked-up data.

## 5. Next step

You can film these yourself, or have them rendered with an AI actor at https://ugcfy.ai.