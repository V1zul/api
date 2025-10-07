from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Any

app = FastAPI()

class DiscoverReq(BaseModel):
    trend_window_hours: int
    max_items: int

class GatherReq(BaseModel):
    claim: str
    max_sources: int

class RankReq(BaseModel):
    claim: str
    sources: List[Any]

class FactReq(BaseModel):
    claim: str
    sources: List[Any]

class DraftReq(BaseModel):
    claim: str
    verdict: str
    findings: List[Any]
    tone: str
    max_tweets: int

class PolishReq(BaseModel):
    tweets: List[str]
    intensity: float

class CiteReq(BaseModel):
    sources: List[Any]
    max_citations: int

@app.post("/discover_topics")
def discover_topics(req: DiscoverReq):
    # TODO: replace with real scrapers/APIs
    return {"items":[
        {"claim":"AI eliminated 30% of entry-level marketing jobs",
         "source_hint":["news","X"], "evidence_status":"unclear",
         "popularity_score":0.81}
    ]}

@app.post("/gather_sources")
def gather_sources(req: GatherReq):
    return {"sources":[
        {"title":"OECD Employment Outlook 2025","url":"https://oecd.org/...","publisher":"OECD","date":"2025-09-14"},
        {"title":"BLS Employment Projections 2024-2034","url":"https://bls.gov/...","publisher":"BLS","date":"2025-08-30"}
    ]}

@app.post("/rank_conflicts")
def rank_conflicts(req: RankReq):
    return {"key_metrics":["exposure","displacement","wage impact","task share"],
            "conflicts":[{"topic":"exposure ≠ job loss","summary":"High exposure doesn’t imply displacement."}],
            "gaps":["No clean post-2024 disaggregation for 'entry-level marketing'."]}

@app.post("/fact_check")
def fact_check(req: FactReq):
    return {"findings":[
        {"statement":"No reputable dataset supports '30% of marketing jobs lost to AI'.",
         "confidence":0.9,"citations":[0,1]}
    ], "verdict":"Misleading", "disclaimer":"Limited disaggregated data."}

@app.post("/draft_thread")
def draft_thread(req: DraftReq):
    t = [
      "1/ You’ve been fed a scary stat. Here are the receipts. 🧵",
      "2/ The claim: 'AI eliminated 30% of entry-level marketing jobs.'",
      "3/ Reality: No official dataset shows a 30% AI-driven cut. Exposure ≠ displacement.",
      "4/ OECD & BLS track exposure and projections—not a 30% AI-only layoff figure.",
      "5/ Anecdotes exist (hiring freezes, task shifts), but they’re not cleanly attributed.",
      "6/ Where AI bites: entry-level task automation (briefs, drafts, A/B ideas).",
      "7/ Where humans still win: strategy, client context, brand voice, channels.",
      "8/ The honest take: tasks shift downward; jobs morph; blanket 30% stat is hype.",
      "9/ Upside: hybrid marketers using AI ship more, faster → better odds of promotion.",
      "10/ Action: skill into prompts, analytics, creative direction, channel ops.",
      "11/ Watch: headcount mix (junior→mid), titles changing to 'AI-enabled' roles.",
      "12/ TL;DR: No, AI didn’t nuke 30% of entry-level marketing jobs. It’s task churn.",
      "13/ Follow for un-hyped AI & jobs research. Weekly report coming soon."
    ]
    return {"tweets": t, "cta":"Follow for un-hyped AI & jobs research."}

@app.post("/polish_style")
def polish_style(req: PolishReq):
    return {"tweets": req.tweets}

@app.post("/assemble_citations")
def assemble_citations(req: CiteReq):
    return {"citations":[
        "[1] OECD Employment Outlook 2025 (Sep 14, 2025)",
        "[2] BLS Employment Projections 2024-2034 (Aug 30, 2025)"
    ]}
