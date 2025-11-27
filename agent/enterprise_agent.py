from .tools import Logger
from .memory import SimpleMemory

class EnterpriseAgent:
    def __init__(self, name="EnterpriseAgent"):
        self.name = name
        self.logger = Logger()
        self.memory = SimpleMemory()

    def analyze_task(self, task):
        t = task.lower()
        if "report" in t:
            return {"task": task, "intent": "generate_report"}
        elif "email" in t or "mail" in t:
            return {"task": task, "intent": "draft_email"}
        elif "inventory" in t or "stock" in t:
            return {"task": task, "intent": "inventory_check"}
        return {"task": task, "intent": "general"}

    def execute_task(self, task):
        analysis = self.analyze_task(task)
        intent = analysis["intent"]

        if intent == "generate_report":
            result = self._generate_report(task)
        elif intent == "draft_email":
            result = self._draft_email(task)
        elif intent == "inventory_check":
            result = self._inventory_check(task)
        else:
            result = {"status": "forwarded", "detail": "Needs human review"}

        self.memory.save({"task": task, "result": result})
        return {"analysis": analysis, "result": result}

    def _generate_report(self, task):
        self.logger.log("Generating report...")
        return {"status": "ok", "report_url": "./data/sample_report.pdf", "note": "stub"}

    def _draft_email(self, task):
        self.logger.log("Drafting email...")
        subject = "Automated: " + (task[:50] + "...")
        body = f"Hello,\n\nThis is an automated draft for request: {task}\n\nRegards,\n{self.name}"
        return {"status": "ok", "subject": subject, "body": body}

    def _inventory_check(self, task):
        self.logger.log("Checking inventory...")
        return {"status": "ok", "items_below_threshold": ["part-A", "part-C"]}


if __name__ == "__main__":
    agent = EnterpriseAgent()
    print(agent.execute_task("Please generate a quarterly sales report"))

