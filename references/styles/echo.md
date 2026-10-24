# 暖纸书卷 · echo

来源：echo-book（回声书稿系统，用户自己的项目）
一句话：旧纸、墨字、紫到玫瑰的暖光，适合“讲一个人”。

## Tokens

```css
:root{
  --paper-top:#fbf7f0;
  --paper-bottom:#f4ede1;
  --ink:#2b2118;
  --muted:#7a6850;
  --line:#eadfc7;
  --card:#fffef7;
  --hover:#f6eede;
  --accent-grad:linear-gradient(135deg, #3a1c71 0%, #d76d77 60%, #ffaf7b 100%);
  --amber:linear-gradient(135deg, #e0a96d, #c06a4a);
  --radius:14px;
}
```

## 字体

- `"PingFang SC", "Microsoft YaHei", sans-serif`
- 标题 600–700，`letter-spacing:2–4px`（中文标题可宽字距）
- 正文 15–17px / 1.8；颜色 `--ink`

## 版式

- 背景：`linear-gradient(180deg, var(--paper-top), var(--paper-bottom))`
- 页面容器 1200px；头部 sticky 白底 + 1px `--line`
- 卡片：`--card` 底、1px `--line`、圆角 14–18、轻阴影
- 强调：标题前的 4px 渐变竖条；按钮用 `--amber`

## 动效

- hover 背景变 `--hover`；180ms
- 不做花哨入场

## 适用 / 不适用

- 适用：传记、纪念页、家族叙事、文学栏目、书稿预览
- 不适用：技术产品、极简工具、深色场景

## 文字密度

高。网页可放完整章节与长引文；deck 用引文页，每页 ≤ 120 字，靠朗读而不是阅读。

## 网页模式

- 纸底渐变满屏；1200px 容器；卡片 + 1px 线
- 标题可加宽字距（2–4px）

## deck 模式

- 纸底满屏；衬线标题 + 引文页
- 用「章节标题 / 一句引文 / 一两个数字」讲人
- 少图表；要数据就一页只放一组
## 反模式

- 冷色、纯黑白极简（没有温度）
- 紫色渐变铺满整页（只用一条）
- 圆角过大（> 20px）失去书卷气
