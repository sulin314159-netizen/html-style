# 书院暖光 · goodpage

来源：goodpage.net/p/ptokzaju（「深极未来 AI 学堂」页面的真实 tokens）
一句话：奶油纸底 + 深青 + 珊瑚金，居中排版，像一张做得极好的学院海报。

## Tokens

```css
:root{
  --paper:#faf8f5;
  --paper-2:#f3f0eb;
  --paper-teal:#eef7f7;
  --ink:#1a1520;
  --muted:#5c5565;
  --faint:#8c8495;
  --teal:#0d7377;
  --teal-light:#14919b;
  --coral:#e8562a;
  --gold:#b87a14;
  --line:#e5e0d8;
  --line-teal:rgba(13,115,119,.12);
  --shadow:0 2px 12px rgba(26,21,32,.05);
}
```

## 字体

- `'PingFang SC', 'Microsoft YaHei', 'Noto Sans SC', sans-serif`
- 标题 700–900；副标 18–20px / 1.6；小标签用 mono，字距 0.12em
- 中文标题用 0 或 +0.02em 字距，不要负字距

## 版式

- 居中 hero：胶囊标签 → 两行大标题（第二行用 `--teal`）→ 一行副标 → 胶囊 CTA → 底部 meta
- 背景只用 `--paper`，可叠一层极淡的青色径向光或同心圆，不抢字
- 内容区：奶油卡片 + 1px `--line` + 12–16px 圆角 + `--shadow`
- **一页只用一个强调色**：`--teal` / `--coral` / `--gold` 三选一，其余是中性色

## 文字密度

中低。hero 一句标题 + 一行说明；网页 400–800 字；deck 每页 ≤ 60 字。留白是主角，字多了就变成普通官网。

## 网页模式

- hero 居中；往下 3 列课程/特性卡，每卡 ≤ 40 字
- 移动端单列，标题降到 40–48px
- 表单/按钮用全圆角胶囊，边框用 `--line-teal`

## deck 模式

- 1280×800 或 1920×1080，居中构图
- 封面：胶囊 + 两行标题 + 副标 + 署名；内容页：一句标题 + 3 张卡
- 不要左对齐长文；这套风格的节奏是“居中、短句、呼吸”

## 反模式

- 冷灰、纯白背景，紫蓝渐变
- 同时出现 teal + coral + gold 三个强调色
- 左对齐长段落（这套是居中的）
- 硬阴影、大圆角卡片
