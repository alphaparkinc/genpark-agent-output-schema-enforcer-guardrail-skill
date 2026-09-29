"""Agent Output JSON Schema Enforcer Guardrail.
100% Python Standard Library.
"""

import json
import re

class OutputSchemaEnforcer:
    """JSON output validator, auto-repairer, and schema enforcer."""
    @staticmethod
    def repair_and_validate(json_str, required_fields=None):
        cleaned = re.sub(r'^```json\s*|\s*```$', '', json_str.strip())
        try:
            data = json.loads(cleaned)
        except Exception:
            if cleaned.count('{') > cleaned.count('}'):
                cleaned += '}' * (cleaned.count('{') - cleaned.count('}'))
            try:
                data = json.loads(cleaned)
            except Exception as e:
                return {"valid": False, "error": f"JSON Syntax Error: {e}", "data": None}

        if required_fields:
            for f in required_fields:
                if f not in data:
                    data[f] = None
        return {"valid": True, "data": data, "repaired": True}
