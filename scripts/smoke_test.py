#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import zipfile
from pathlib import Path

from render_bundle import render_bundle
from template_rewriter import build_spec


def count_media(docx_path: Path) -> int:
    with zipfile.ZipFile(docx_path) as archive:
        return len([name for name in archive.namelist() if name.startswith("word/media/") and not name.endswith("/")])


def main() -> None:
    spec = build_spec(
        "校园志愿服务管理平台",
        "这是一个面向高校的 Web 管理系统，支持志愿活动发布、报名审核、信息录入、查询统计、互动交流和后台管理。",
    )
    with tempfile.TemporaryDirectory(prefix="softcopy-smoke-") as temp_dir:
        output_dir = Path(temp_dir)
        result = render_bundle(spec, output_dir)

        required_files = [
            Path(result["spec_path"]),
            Path(result["application_path"]),
            Path(result["manual_path"]),
            Path(result["code_path"]),
        ]
        for path in required_files:
            if not path.exists():
                raise FileNotFoundError(f"Missing generated file: {path}")

        mockup_files = sorted(Path(result["mockup_dir"]).glob("*.*"))
        if len(mockup_files) != 16:
            raise RuntimeError(f"Expected 16 mockups, got {len(mockup_files)}")

        if result["source_line_count"] < 3200:
            raise RuntimeError(f"Expected at least 3200 non-empty code lines, got {result['source_line_count']}")

        manual_media = count_media(Path(result["manual_path"]))
        if manual_media != 16:
            raise RuntimeError(f"Expected 16 embedded manual images, got {manual_media}")

        print(
            json.dumps(
                {
                    "ok": True,
                    "generated_files": [str(path.name) for path in required_files],
                    "mockup_count": len(mockup_files),
                    "manual_media": manual_media,
                    "source_line_count": result["source_line_count"],
                },
                ensure_ascii=False,
                indent=2,
            )
        )


if __name__ == "__main__":
    main()
