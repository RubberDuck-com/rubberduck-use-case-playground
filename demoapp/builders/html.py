"""HTML builder — UC-08, UC-09, UC-10 sample methods."""

from __future__ import annotations

import os
from typing import Any

from demoapp.application import Application, BuildInfo


class Builder:
    parallel_read_safe = False
    parallel_write_safe = False
    search = True

    def __init__(self, app: Application) -> None:
        self.app = app
        self.config = app.config
        self.env = app.env
        self.globalcontext: dict[str, Any] = {}

    def build(self, docnames: list[str]) -> None:
        for docname in docnames or ["index"]:
            self.write_doc(docname)

    def write_doc(self, docname: str) -> None:
        self.prepare_writing([docname])
        self.handle_page(docname)

    def prepare_writing(self, docnames: list[str]) -> None:
        raise NotImplementedError

    def handle_page(self, docname: str) -> None:
        pass

    def get_outdated_docs(self) -> list[str]:
        raise NotImplementedError


class StandaloneHTMLBuilder(Builder):
    def newest_template_mtime(self) -> float:
        return 0.0

    def doc2path(self, docname: str) -> str:
        return os.path.join(self.app.srcdir, f"{docname}.rst")

    def get_outfilename(self, docname: str) -> str:
        return os.path.join(self.app.srcdir, "_build", f"{docname}.html")

    def render_partial(self, node: dict[str, Any] | None) -> dict[str, str]:
        """13-line utility — UC-10 quick check target."""
        if node is None:
            return {"fragment": ""}
        return {"fragment": f"<p>{node.get('text', '')}</p>"}

    def get_doc_context(self, docname: str) -> dict[str, str]:
        title_node = {"text": docname}
        return {
            "title": self.render_partial(title_node)["fragment"],
            "toc": self.render_partial({"text": "toc"})["fragment"],
        }

    def handle_page(self, docname: str) -> None:
        context = self.get_doc_context(docname)
        outfile = self.get_outfilename(docname)
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
        project = self.globalcontext.get("project", "demo")
        version = self.globalcontext.get("version", "0.0.0")
        html = (
            "<!DOCTYPE html>\n"
            f"<html>\n<head><title>{project}: {docname}</title></head>\n"
            "<body>\n"
            f"<h1>{context['title']}</h1>\n"
            f"<nav>{context['toc']}</nav>\n"
            f"<footer>{project} v{version}</footer>\n"
            "</body>\n</html>\n"
        )
        with open(outfile, "w", encoding="utf-8") as handle:
            handle.write(html)
        self.last_outfile = outfile

    def write_doc_serialized(self, docname: str) -> dict[str, str]:
        return {"title": self.render_partial({"text": docname})["fragment"]}

    def _get_local_toctree(self, docname: str) -> str:
        return self.render_partial({"text": "local"})["fragment"]

    def prepare_writing(self, docnames: list[str]) -> None:
        self.globalcontext = {
            "project": self.config.config_values.get("project", "demo"),
            "version": "0.1.0",
        }

    def get_outdated_docs(self) -> list[str]:
        """Staleness logic — UC-08 logic check target."""
        outdated: list[str] = []
        buildinfo_path = os.path.join(self.app.srcdir, ".buildinfo")
        buildinfo = BuildInfo.create(self.config, self.app.tags)
        if os.path.exists(buildinfo_path):
            previous = BuildInfo.load(buildinfo_path)
            if buildinfo != previous:
                return list(self.env["all_docs"].keys()) or ["index"]

        for docname in self.env["all_docs"]:
            if docname not in self.env["all_docs"]:
                outdated.append(docname)
                continue
            try:
                targetmtime = os.path.getmtime(self.get_outfilename(docname))
            except OSError:
                targetmtime = 0
            srcmtime = max(
                os.path.getmtime(self.doc2path(docname)),
                self.newest_template_mtime(),
            )
            if srcmtime > targetmtime:
                outdated.append(docname)
        return outdated


THEME_WRITING_MODES = {
    "vertical": "vertical-rl",
    "horizontal": "horizontal-tb",
}


class Epub3Builder(StandaloneHTMLBuilder):
    search = False
    html_tag = '<html xmlns:epub="http://www.idpf.org/2007/ops">'
    use_meta_charset = True
    skip_ua_compatible = True

    def prepare_writing(self, docnames: list[str]) -> None:
        super().prepare_writing(docnames)
        mode = self.config.config_values.get("epub_writing_mode", "horizontal")
        self.globalcontext["theme_writing_mode"] = THEME_WRITING_MODES.get(mode, "horizontal-tb")
        self.globalcontext["html_tag"] = self.html_tag
        self.globalcontext["use_meta_charset"] = self.use_meta_charset
        self.globalcontext["skip_ua_compatible"] = self.skip_ua_compatible
