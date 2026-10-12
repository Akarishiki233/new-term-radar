"""Report text in English and Chinese. t("key", name=value) fills the template of the
language set in config.json ("lang": "en" or "zh")."""
from __future__ import annotations

_LANG = "en"

T = {
    # notes on a lead, one per signal
    "note_x": ("X: {n} accounts, {likes} likes", "X {n} 个账号 ♥{likes}"),
    "note_hf": ("Hugging Face: new at #{rank}", "HF 新进榜第 {rank} 名"),
    "note_hf_copies": (", {n} versions", ",{n} 个版本"),
    "note_breakout": ("GitHub breakout {repo} ★{stars} ({velocity}/day{gain})", "GitHub 爆发 {repo} ★{stars}(均 {velocity}/天{gain})"),
    "note_breakout_gain": (", +{delta} in a day", ",一天 +{delta}"),
    "note_site": ("New site {domain} (registered {created}, ~{etv} visits/mo, {keywords} ranking keywords)",
                  "新站 {domain}(注册 {created},约 {etv} 访问/月,{keywords} 个排名词)"),
    "note_surge": ("{label}: {n} places (×{lift})", "{label} {n} 处 (×{lift})"),
    # signal labels, earliest first
    "kind_x": ("① X", "① X"), "kind_hf": ("① HF", "① HF"), "kind_breakout": ("② breakout", "② 爆发"),
    "kind_sitemap": ("③ sitemaps", "③ 竞品"), "kind_newsite": ("③ new site", "③ 新站"), "kind_watch": ("watch", "观察词"),
    # daily report
    "title": ("## New-term radar", "## 新词雷达"),
    "leads_h": ("### Candidate new terms (names first; terms you already cover are marked)",
                "### 候选新词(判为专有名词的排前面;已覆盖的会标出)"),
    "leads_cols": ("| Term | Signals | Name score | Known | Search variants | Examples |", "| 词 | 信号 | 名字得分 | 已覆盖 | 搜索变体 | 例子 |"),
    "none": ("none", "无"), "dash": ("—", "—"),
    "other_terms": ("Other rising terms (judged common words): ", "其他上升词(判为普通词):"),
    "topic_h": ("### Topic: {name}", "### 主题:{name}"),
    "topic_none": ("Nothing new on this topic today", "今天没有相关的新词"),
    "topic_lead": ("- Candidate **{term}**: {signals}", "- 候选词 **{term}**:{signals}"),
    "topic_repo": ("- Breakout repo [{repo}](https://github.com/{repo}) ★{stars} ({velocity}/day): {desc}",
                   "- 爆发仓库 [{repo}](https://github.com/{repo}) ★{stars}(均 {velocity}/天):{desc}"),
    "topic_query": ("- New query `{query}`: {impressions} impressions, landing on {page}", "- GSC 新词 `{query}`:曝光 {impressions},落地页 {page}"),
    "recent_h": ("### ① Source leads of the last 24 hours (kept by the frequent job)", "### ① 近 24 小时的源头新词(高频任务记下的)"),
    "recent_none": ("None ({why})", "无({why})"), "no_new_names": ("no new names", "没有新名字"),
    "breakout_h": ("### ② Single-repo breakouts (created in the last {days} days, by stars a day; 🆕 = first day above the bar)",
                   "### ② 单仓库爆发(近 {days} 天新建,按每天涨星排;🆕 = 今天第一次达标)"),
    "breakout_cols": ("| Repo | ★ | Per day | Since yesterday | Age (days) | About |", "| 仓库 | ★ | 均/天 | 比昨天 | 天数 | 简介 |"),
    "no_breakouts": ("no breakout repos", "没有爆发仓库"), "skipped": ("skipped", "跳过"),
    "newsite_h": ("### ③ New sites (registered and first indexed in the last {days} days, est. visits/mo >{etv}, ≥{kw} ranking keywords; 🆕 = first seen)",
                  "### ③ 新站(近 {days} 天注册且首次被收录、月访问估值 >{etv}、排名词 ≥{kw};🆕 = 第一次出现)"),
    "newsite_cols": ("| Domain | Registered | First indexed | Visits/mo (est.) | Ranking keywords |", "| 域名 | 注册 | 首次收录 | 访问/月(估) | 排名词 |"),
    "newsite_none": ("no qualifying new sites this week", "这周没有符合条件的新站"),
    "gsc_h": ("### ④ Search Console queries seen for the first time (fresh data, about a day behind)", "### ④ GSC 首次出现的搜索词(新鲜数据,约晚 1 天)"),
    "gsc_intro": ("{window}: {total} new queries; those with ≥{min} impressions:", "{window},共 {total} 个新词,曝光 ≥{min} 的:"),
    "gsc_cols": ("| Query | Impressions | Clicks | Landing page |", "| 搜索词 | 曝光 | 点击 | 落地页 |"),
    "gsc_none": ("no new queries", "没有新词"), "gsc_off": ("not configured", "未配置"),
    "review_h": ("### ⑤ Review (terms reported {days} days ago: did they rise in Google Trends?)", "### ⑤ 复盘({days} 天前报出的词,在 Google Trends 里起没起来)"),
    "review_cols": ("| Term | First reported | Verdict | Days ahead |", "| 词 | 首次报出 | 结论 | 提前天数 |"),
    "review_none": ("No term is due today ({why})", "今天没有到期的词({why})"),
    "review_young": ("the oldest lead is under {days} days old", "最早报出的词还不满 {days} 天"),
    "hit_intro": ("Hit rate over the last {days} days ({pending} awaiting review):", "近 {days} 天的命中率(待复盘 {pending} 个):"),
    "hit_cols": ("| Signal | Reviewed | Hits | Hit rate | Median days ahead |", "| 信号 | 复盘 | 命中 | 命中率 | 提前天数中位数 |"),
    "status_h": ("### Data status", "### 数据状态"),
    "st_x": ("- ① X: {state}", "- ① X:{state}"), "st_hf": ("- ① HF: {state}", "- ① HF:{state}"),
    "st_x_ok": ("{answered}/{accounts} accounts, {posts} posts", "{answered}/{accounts} 个账号,{posts} 条帖子"),
    "st_x_first": (", first run: vocabulary built, nothing reported", ",首次运行,只建词表"),
    "st_hf_ok": ("{models} trending models", "trending {models} 个模型"),
    "st_first": (", first run: snapshot built", ",首次运行,只建快照"),
    "st_breakout": ("- ② breakouts: {state}", "- ② 爆发:{state}"),
    "st_breakout_ok": ("{n} new repos searched", "搜到 {n} 个新仓库"),
    "st_breakout_first": (", first run: no star counts from yesterday", ",首次运行,没有昨天的星数"),
    "st_site": ("- ③ {site}: {state}", "- ③ {site}:{state}"),
    "st_site_ok": ("{urls} URLs, {new} new", "{urls} 个网址,新增 {new}"),
    "st_site_first": ("first run: snapshot built", "首次运行,只建快照"),
    "st_sitemaps": ("- ③ sitemaps: {state}", "- ③ 竞品:{state}"),
    "st_record": ("- saving leads: {state}", "- 记录候选词:{state}"),
    "st_judge": ("- name judge: {state}", "- 名字判断:{state}"),
    "cost": ("- AIsa data spend this run: {cost} (the name judge's tokens are billed apart)", "- 本次 AIsa 数据花费:{cost}(名字判断的模型调用另计)"),
    # sources report
    "sources_title": ("## New-term radar · ① sources", "## 新词雷达 · ① 源头"),
    "sources_cols": ("| Term | Signals | Name score | Known | Examples |", "| 词 | 信号 | 名字得分 | 已覆盖 | 例子 |"),
    "posts_h": ("### The posts", "### 推文原文"), "post_link": (" · [post]({url})", " · [原推]({url})"),
    "sources_quiet": ("① no new names: ", "① 没有新名字:"),
}


def set_lang(lang: str) -> None:
    global _LANG
    _LANG = "zh" if str(lang).lower().startswith("zh") else "en"


def t(key: str, **kw) -> str:
    return T[key][_LANG == "zh"].format(**kw)
