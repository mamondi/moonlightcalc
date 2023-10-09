import flet as ft

def main(page:ft.Page):
    page.title = "Калькулятор"
    page.window_height = 360
    page.window_width = 300
    page.update()

    def btn_clicked(a):
        data = a.control.data
        if data in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "(", ")", "."]:
            tfield.value = str(tfield.value) + str(data)
            page.update()

        if data == "=":
            tfield.value = str(eval(tfield.value))
            page.update()

        if data == "a":
            st = list(tfield.value)
            st.pop()
            tfield.value = "".join(map(str, st))
            page.update()

        if data == "C":
            tfield.value = ""
            page.update()

    tfield = ft.TextField(read_only=True, border_color="#003ea3", border_width="2", border_radius=10, text_style=ft.TextStyle(size=30, color="#bfc9d9"))
    page.add(tfield)


    btn_a = ft.ElevatedButton(
        text="<", bgcolor="#0C356A", color="#0061ff", data="a", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_b = ft.ElevatedButton(
        text="(", bgcolor="#0C356A", color="#0061ff", data="(", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_c = ft.ElevatedButton(
        text=")", bgcolor="#0C356A", color="#0061ff", data=")", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_d = ft.ElevatedButton(
        text="÷", bgcolor="#0C356A", color="#0061ff", width=70, data="/", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    r1 = ft.Row(
        controls=[btn_a, btn_b, btn_c, btn_d],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )



    btn_7 = ft.ElevatedButton(
        text="7", bgcolor="#14171c", color="#0061ff", data="7", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_8 = ft.ElevatedButton(
        text="8", bgcolor="#14171c", color="#0061ff", data="8", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_9 = ft.ElevatedButton(
        text="9", bgcolor="#14171c", color="#0061ff", data="9", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_x = ft.ElevatedButton(
        text="*", bgcolor="#0C356A", color="#0061ff", width=70, data="*", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    r2 = ft.Row(
        controls=[btn_7, btn_8, btn_9, btn_x],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )



    btn_4 = ft.ElevatedButton(
        text="4", bgcolor="#14171c", color="#0061ff", data="4", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_5 = ft.ElevatedButton(
        text="5", bgcolor="#14171c", color="#0061ff", data="5", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_6 = ft.ElevatedButton(
        text="6", bgcolor="#14171c", color="#0061ff", data="6", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_mns = ft.ElevatedButton(
        text="-", bgcolor="#0C356A", color="#0061ff", width=70, data="-", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    r3 = ft.Row(
        controls=[btn_4, btn_5, btn_6, btn_mns],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )



    btn_1 = ft.ElevatedButton(
        text="1", bgcolor="#14171c", color="#0061ff", data="1", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_2 = ft.ElevatedButton(
        text="2", bgcolor="#14171c", color="#0061ff", data="2", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_3 = ft.ElevatedButton(
        text="3", bgcolor="#14171c", color="#0061ff", data="3", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_pls = ft.ElevatedButton(
        text="+", bgcolor="#0C356A", color="#0061ff", width=70, data="+", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    r4 = ft.Row(
        controls=[btn_1, btn_2, btn_3, btn_pls],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )



    btn_C = ft.ElevatedButton(
        text="C", bgcolor="#0C356A", color="#0061ff", data="C", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_0 = ft.ElevatedButton(
        text="0", bgcolor="#14171c", color="#0061ff", data="0", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_dot = ft.ElevatedButton(
        text=".", bgcolor="#0C356A", color="#0061ff", data=".", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    btn_eq = ft.ElevatedButton(
        text="=", bgcolor="#005db2", color="#A6F6FF", width=70, data="=", on_click=btn_clicked,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5))
    )
    r5 = ft.Row(
        controls=[btn_C, btn_0, btn_dot, btn_eq],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    page.add(r1, r2, r3, r4, r5)

ft.app(target=main)
