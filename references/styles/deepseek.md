# 技术蓝 · deepseek

来源：deepseek.com（线上 CSS 变量）
一句话：干净的技术蓝，用细边框和玻璃感说“可信”。

## Tokens

```css
:root{
  --bg:#f9f8f8;
  --surface:#ffffff;
  --ink:#1e232c;
  --muted:rgba(0,0,0,.65);
  --brand:#4d6bfe;
  --brand-deep:#3a65c2;
  --dark:#1a1615;
  --line:rgba(0,0,0,.1);
  --line-subtle:rgba(0,0,0,.06);
  --glass:rgba(255,255,255,.45);
  --radius:24px;
  --radius-panel:16px;
  --radius-sm:8px;
  --shadow:0 0 0 1px #f1f5f9, 0 2px 4px rgba(0,0,0,.05), 0 12px 24px rgba(0,0,0,.05);
}
```

## 字体

- `"DM Sans", "Host Grotesk", system-ui, "PingFang SC", "Microsoft YaHei", sans-serif`
- 等宽：`"Fragment Mono", "Roboto Mono", ui-monospace`
- 标题 600，字距 -0.02em；正文 16–17px / 1.7

## 版式

- 容器 1200px；区块间距 96–120px
- 卡片：白底 + 1px `--line` + `--shadow`；圆角 16–24
- 允许一处玻璃面板（`backdrop-filter: blur(12px)`），不要整页玻璃
- 强调色只用 `--brand`；链接、选中态、小标签都用它

## 动效

- 150–200ms 过渡；hover 边框变深
- 不做大幅位移

## 适用 / 不适用

- 适用：开发者工具、AI 产品、文档、后台
- 不适用：纪念类、文学类、活动页

## 文字密度

中。每节 2–4 句；deck 每页 ≤ 90 字。技术说明可以多，但每段只讲一件事。

## 网页模式

- 1200px 容器；白卡 + 1px 细边框；玻璃最多一处
- 品牌蓝只给链接、选中态、小标签

## deck 模式

- 白底幻灯片；`--brand` 只给关键词和数字
- mono 做 eyebrow（12–14px，字距 .2em）
- 标题 60–80px；一页一个结论 + 一行支撑 + ≤3 个数据
## 反模式

- 粗黑边框、饱和背景块、衬线标题
- 玻璃拟态滥用（超过两处）
- 用 `--brand` 大面积铺底
