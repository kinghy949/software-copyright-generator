---
name: software-copyright-generator
description: "Generate a software copyright registration material bundle for common Web systems. Use when the user asks for 软著, 软件著作权, 申请表, 操作手册, 代码文档, 三件套, or wants to generate copyright application materials from only a software name and a short Chinese system introduction. This skill creates three .docx files in a fixed Java/Vue-style template: application form draft, operation manual with matching mock screenshots, and code document."
---

# Software Copyright Generator

## Overview

Generate a fixed-format soft copyright bundle for common Web systems from two inputs only: `系统全名` and `系统简介`.
Use the bundled Python scripts to create three `.docx` files plus screenshot assets in one pass.

## Quick Start

Run the main renderer directly:

```powershell
python "C:\Users\PC\.codex\skills\software-copyright-generator\scripts\render_bundle.py" `
  --name "校园志愿服务管理平台" `
  --intro "这是一个面向高校的 Web 管理系统，支持志愿活动发布、报名审核、数据统计和后台管理。" `
  --output-dir ".\softcopy-output"
```

The command writes:

- `基于SpringBoot的<系统名>_申请表.docx`
- `基于Java&Vue的<系统名>_操作手册.docx`
- `基于Java&Vue的<系统名>_代码文档.docx`
- `<系统名>_spec.json`
- `mockups/` with 16 generated images

## Workflow

### 1. Collect The Two Required Inputs

Require only:

- `系统全名`
- `系统简介`

Do not ask for extra metadata unless the user explicitly wants manual edits after generation.

### 2. Render The Bundle

Use `scripts/render_bundle.py`.
This script does all generation steps:

1. Build an internal spec from the name and introduction
2. Generate 16 screenshot-style images
3. Fill the application form template
4. Rewrite the operation manual text and replace the embedded images
5. Generate a 60+ page code document in the fixed Java/Vue style

### 3. Report Output Paths

Return the absolute output directory and the three `.docx` file paths.
Keep the response concise.

## Output Shape

The bundle is intentionally fixed-format:

- `申请表` uses the bundled single-page table layout
- `操作手册` keeps the current 6-module, 19-page style structure
- `代码文档` keeps the Java/Vue technical style and large line count

The generated screenshots are programmatic mockups, not real product captures.

## Defaults

The scripts use stable defaults without asking the user:

- Version: `V1.0`
- 权利取得方式: `原始取得`
- 权利范围: `全部权利`
- 软件分类: `应用软件`
- 软件说明: `原创`
- 开发方式: `单独开发`
- 发表状态: `未发表`
- 技术栈文风: `Java 17 + Spring Boot 3 + Vue + MySQL`

The output targets common Web systems such as campus systems, management platforms, information systems, and service portals.

## Files

### `scripts/render_bundle.py`

Main entry point. Use this script unless you are debugging a sub-step.

### `scripts/template_rewriter.py`

Build the internal content spec and the long-form code lines.

### `scripts/render_mockups.py`

Generate the 16 screenshot-like images used by the operation manual.

### `references/requirements.md`

Read this only when the user asks about formal requirements, review points, or 审查风险.

### `assets/templates/`

Contains the `.docx` templates copied from the existing material set.

## Practical Notes

- Treat this skill as a fast fixed-template generator, not an official filing system.
- Keep the generated files editable. Users often revise names, dates, and wording after first pass.
- If the user wants stricter legal compliance, read `references/requirements.md` and explain the gap between generated drafts and formal submission review.
