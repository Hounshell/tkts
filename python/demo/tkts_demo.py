from tkts.models import facts, schema
from tkts import Ticket
from tkts.storage import MemoryStorage


print("Hello world")

priority = facts.IntegerFact("Priority", validation=lambda v: 0 <= v < 5);
severity = facts.IntegerFact("Severity", validation=lambda v: 0 <= v < 5);
subject = facts.StringFact("Subject", required=True);
creator = facts.StringFact("Creator");
assignee = facts.RepeatedStringFact("Assignee");
modified_by = facts.StringFact("ModifiedBy");
pii = facts.StringFact("PII");

basic_schema = schema.Schema(
    "basic", 
    facts=[priority, severity, subject, creator, assignee, modified_by, pii]);

storage = MemoryStorage([basic_schema])
ticket = storage.commit(Ticket.create(schema, "Creating a new ticket")
    .set_fact(modified_by, "alice")
    .set_fact(priority, 2)
    .set_fact(severity, 4)
    .set_fact(subject, "Demo issue")
    .set_fact(creator, "dan")
    .set_fact(assignee, ["alice", "bob", "carol"])
    .set_fact(pii, "Age: 47"))

storage.commit(ticket
    .update("Updating an existing ticket")
    .set_fact(modified_by, "dan")
    .set_fact(subject, "Example Issue")
    .set_fact(assignee, List.of("alice", "bob", "carol", "dan"))
    .remove_fact(severity)
    .redact_fact(pii)
    .redact_update(ticket.updates[0]));

storage.commit(ticket.redact());

print(ticket.id)
print(ticket[fact])
print(ticket.schema)
print(ticket.updates)
print(ticket.updates[0].changes)
print(ticket.updates[0].changes[0].fact)
print(ticket.updates[0].changes[0].old_value)
print(ticket.updates[0].changes[0].new_value)
print(ticket.updates[0].changes[0].id_old_value_redacted)
print(ticket.updates[0].changes[0].id_new_value_redacted)

print(storage.fetch(ticket.id))
print(storage.query("modified_by: dan"))

