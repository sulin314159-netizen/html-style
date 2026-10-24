# 纸感极简 · moneyai

来源：moneyai.lat（用户最爱的极简风，线上抓的真实 tokens）
一句话：像一张好纸，安静、可信、留白大于内容。

## Tokens

```css
:root{
  --paper:#fbfaf6;
  --card:#ffffff;
  --ink:#16201e;
  --muted:#5d6865;
  --line:#e5e7df;
  --green:#008c68;
  --green-dark:#05664f;
  --mint:#dff4eb;
  --amber:#e28a2b;
  --blue:#286d91;
  --navy:#102c27;
  --radius:20px;
  --max:1160px;
  --shadow:0 20px 55px -35px rgba(9,50,42,.42);
}
```

**强调色只有 `--green`**；`--amber`、`--blue` 是辅助信息色，一页最多出现一处，不用于按钮和链接。文字链接用 `--green-dark`（`--green` 在纸底上只有 4.06:1，不达标）。`--green` 实底白字只有 4.24:1，按钮请用 `--green-dark` 或把按钮文字做到 ≥19px 粗体。

## 字体

- 正文/UI：`Inter, "Segoe UI", system-ui, -apple-system, sans-serif`
- 中文：`"PingFang SC", "Microsoft YaHei", sans-serif`
- 标题 600–700；西文 `letter-spacing:-.02em`，中文标题用 `0` 或 `+.02em`（负字距会让中文变挤）
- 数字：默认 lining，不用旧式数字

## 版式

- 单栏为主，`max-width:1160px`，左右留白 ≥ 5vw
- 区块间距 80–120px；标题到正文 16–24px
- 卡片很少；分隔优先用 1px `--line`，不是阴影
- 正文宽度 65–75ch

## 组件

- 主按钮：`--green-dark` 实底、白字、圆角 12 或 pill；hover 用 `#044c3c`
- 次按钮：白底、1px `--line`、`--ink` 字
- 标签：`--mint` 底 + `--green-dark` 字
- 链接：`--green-dark`，下划线 offset 4

## 动效

- 只做 hover/focus，120–180ms `ease-out`
- 不做入场动画、不做视差

## 适用 / 不适用

- 适用：产品页、长文、文档、作品集、定价页
- 不适用：活动页、需要“热闹”的营销页、深色场景

## 文字密度

中高。网页可承载 800–1500 字的说明/长文；deck 每页 ≤ 80 字。写不满就补事实、口径、边界，不要补水词。

## 网页模式

- 1160px 容器；区块 88–120px；正文 65–75ch
- 卡片少、用 1px 线分隔；移动端单栏
- 按钮 `--green-dark` 实底白字；链接也用 `--green-dark`

## deck 模式

- 16:9；纸底不变，留白更大；一页一个论点
- 标题 `min(7vw,11vh)`；正文 ≥ 24px；三列数据用 Inter lining
- 不用卡片网格；一条发丝线 + 三个数字 + 一句结论
## 反模式

- 紫蓝渐变、玻璃拟态、重阴影、彩色插画
- 三张一模一样的卡片排一排
- 同时出现两个以上强调色
