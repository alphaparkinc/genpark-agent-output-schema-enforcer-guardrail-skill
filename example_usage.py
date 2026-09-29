from client import OutputSchemaEnforcer

malformed = '```json\n{"status": "success", "user_id": 42'
res = OutputSchemaEnforcer.repair_and_validate(malformed, required_fields=["status", "user_id", "email"])

print("Valid:", res["valid"])
print("Repaired JSON Object:", res["data"])
