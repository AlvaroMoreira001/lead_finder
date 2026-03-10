from playwright.sync_api import sync_playwright

import asyncio
import sys

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())


class BrowserManager:

    def start(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )

        self.context = self.browser.new_context()

        return self.context.new_page()

    def close(self):

        self.browser.close()
        self.playwright.stop()
