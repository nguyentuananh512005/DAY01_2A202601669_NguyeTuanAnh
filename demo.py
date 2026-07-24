"""Demo run_assistant voi Gemini API thuc te."""
from template import run_assistant

# 3 cau hoi tu dong
inputs = iter([
    "Blockchain la gi? Tra loi ngan gon.",
    "No co lien quan gi den tien ao?",
    "Cam on ban!",
    "quit"
])

print("=" * 50)
print("DEMO TRO LY CLI - GEMINI API")
print("=" * 50)
print()

stats = run_assistant(
    persona="Ban la tro giang than thien cua khoa AI, tra loi ngan gon bang tieng Viet.",
    get_input=lambda: next(inputs),
    max_turns=3
)

print()
print("=" * 50)
print("THONG KE PHIEN CHAT")
print("=" * 50)
print(f"So luot hoi-dap: {stats['num_turns']}")
print(f"Tong token:      {stats['total_tokens']}")
print(f"Tong chi phi:    ${stats['total_cost']:.6f}")
print(f"History length:  {len(stats['history'])} messages")
print()
for msg in stats['history']:
    role = msg['role'].upper()
    content = msg['content'][:150]
    print(f"[{role}] {content}...")
