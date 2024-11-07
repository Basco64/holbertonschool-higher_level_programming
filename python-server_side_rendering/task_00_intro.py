import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("Error: No attendees provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = (attendee.get(key, "N/A") if attendee.get(key) is not None
                     else "N/A")
            content = content.replace(f"{{{key}}}", value)

        filename = f"./tests/output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(content)

        print(f"File {filename} created successfully.")
