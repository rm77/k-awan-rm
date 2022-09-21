import flet
from flet import Card, Column, Container, Icon, ListTile, Row, Text, TextButton, icons
import requests

ENDPOINT_URL='http://127.0.0.1:32000/notepads'

def get_notepad_data():
    r = requests.get(ENDPOINT_URL)
    code = r.status_code
    if (code==200):
        print(r.json())
        result = r.json()['data']
        return result
    else:
        return []


def main(page):
    page.title = "Card Example"
    for d in get_notepad_data():
        xdata = d['data']
        content = xdata['content']
        tanggal = xdata['date']
        card = Card(
                    content=Container(
                        content=Column(
                                [
                                    ListTile(
                                        leading=Icon(icons.ALBUM),
                                        title=Text(tanggal),
                                        subtitle=Text(
                                            content
                                        ),
                                    ),
                                    Row(
                                        [TextButton("Delete"), TextButton("Edit")],
                                        alignment="end",
                                    ),
                                ]
                                ),
                        width=400,
                        padding=10,
                    )
                )
        page.add(card)

flet.app(target=main, view=flet.WEB_BROWSER)
