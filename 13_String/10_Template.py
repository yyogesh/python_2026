from string import Template

# Safe for user-supplied templates (no code execution possible)
t = Template('Hello, $name! You have $count messages.')

print(t.safe_substitute(name='Alice', count=5))  # Hello, Alice! You have 5 messages.

# Real use: email templates where users edit the template
email_template = Template(
    'Dear $first_name,\n'
    'Your order $order_id is ready.\n'
    'Estimated delivery: $delivery_date'
)
print(email_template.substitute(
    first_name='Rohan',
    order_id='ORD-2024-001',
    delivery_date='2024-03-15'
))