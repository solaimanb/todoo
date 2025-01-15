import flet as ft


def main(page: ft.Page):
    # Set the page theme & styling
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(scrollbar_theme=ft.ScrollbarTheme(thickness=3))
    page.title = "TODOO!"
    page.bgcolor = ft.colors.SURFACE

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Store tasks
    tasks = []

    # Function to handle adding tasks
    def add_task(e):
        if not task_input.value.strip():
            task_input.error_text = "Please enter a task."
        else:
            task_input.error_text = ""
            task = ft.Checkbox(
                label=task_input.value,
                on_change=toggle_task,
                label_style=ft.TextStyle(
                    weight=ft.FontWeight.W_600,
                    color=ft.colors.ON_SURFACE,
                ),
            )
            tasks.append(task)
            task_list.controls.append(task)
            task_input.value = ""

        task_input.update()
        task_list.update()

    # Function to toggle task completion
    def toggle_task(e):
        e.control.label_style = ft.TextStyle(
            color=ft.colors.GREEN if e.control.value else ft.colors.INVERSE_SURFACE,
            weight=ft.FontWeight.BOLD,
        )
        e.control.update()

    # Function to clear completed tasks
    def clear_completed(e):
        task_list.controls = [task for task in tasks if not task.value]
        task_list.update()

    # Scroll event handler
    def on_task_scroll(e: ft.OnScrollEvent):
        pass

    # Initialize UI elements
    task_input = ft.TextField(
        hint_text="What needs to be done?",
        width=300,
        bgcolor=ft.colors.SURFACE_VARIANT,
        border_radius=5,
        content_padding=10,
        color=ft.colors.ON_SURFACE,
        text_style=ft.TextStyle(size=16),
        on_submit=add_task,
    )
    add_button = ft.ElevatedButton(
        "+",
        width=40,
        height=44,
        on_click=add_task,
        bgcolor=ft.colors.SECONDARY_CONTAINER,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
    )
    clear_button = ft.ElevatedButton(
        "Clear Completed",
        icon=ft.icons.DELETE_OUTLINE,
        on_click=clear_completed,
        bgcolor=ft.colors.SURFACE_VARIANT,
        color=ft.colors.ON_SURFACE,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
    )

    # Scrollable task list
    task_list = ft.Column(
        spacing=10,
        scroll=ft.ScrollMode.ALWAYS,
        height=300,
        on_scroll=on_task_scroll,
    )

    # Add UI elements to the page
    page.add(
        ft.Container(
            ft.Column(
                [
                    ft.Text(
                        "TODOO!",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.ON_SURFACE,
                    ),
                    ft.Row(
                        [task_input, add_button],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        spacing=10,
                    ),
                    ft.Divider(height=10),
                    ft.Container(
                        content=task_list,
                        expand=True,
                        height=300,
                        padding=10,
                        bgcolor=ft.colors.SURFACE,
                        border_radius=5,
                    ),
                    ft.Row(
                        [clear_button],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=400,
            padding=20,
            bgcolor=ft.colors.BACKGROUND,
            border_radius=5,
            shadow=ft.BoxShadow(blur_radius=5, spread_radius=1, color=ft.colors.BLACK),
        )
    )


ft.app(main)
