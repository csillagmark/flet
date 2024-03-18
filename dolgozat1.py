import flet as ft


def doga1(page: ft.Page):
    page.title = "dolgozat"
    page.scroll = ft.ScrollMode.AUTO

    feladat1 = ft.Row(
        [
            ft.Text(
                value = "hello",
            ),
            ft.Text(
                value = "world",
            ),
        ],
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    )
    
    feladat2 = ft.Container(
        content = ft.Text(
            value = "a"
        ),
        bgcolor = ft.colors.BLUE,
        height = 200,
        alignment = ft.alignment.center,
        margin = ft.margin.all(0),
        padding = ft.padding.all(0),
    )

    feladat3 = ft.Row(
        [
            ft.Container(
                height = 200,
                width = 200,
                bgcolor = ft.colors.YELLOW,
                margin = ft.margin.only(left = 10),
            ),
            ft.Container(
                height = 200,
                width = 200,
                bgcolor = ft.colors.BLUE,
                margin = ft.margin.only(left = 10),
            ),
            ft.Container(
                height = 200,
                width = 200,
                bgcolor = ft.colors.GREEN,
                margin = ft.margin.only(left = 10),
            ),
            ft.Container(
                height = 200,
                width = 200,
                bgcolor = ft.colors.BLACK,
                margin = ft.margin.only(left = 10),
            ),
            ft.Container(
                height = 200,
                width = 200,
                bgcolor = ft.colors.RED,
                margin = ft.margin.only(left = 10),
            ),
        ],
    )

    page.add(feladat1, feladat2, feladat3)
    page.update()


ft.app(target = doga1)
