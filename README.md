# TODOO! App

A simple task management app built using [Flet](https://flet.dev).

## Features

- Add tasks
- Mark tasks as completed
- Clear completed tasks
- Scrollable task list

## Requirements

- Python 3.7 or higher
- Flet framework

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/solaimanb/todoo.git
   cd todoo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

Run the app locally:
```bash
 flet run todoo.py
```

For web view, update the last line in `main.py`:
```python
ft.app(target=main, view=ft.WEB_BROWSER)
```

## Building an APK

Follow these steps to build an APK for Android:
1. Install [Buildozer](https://github.com/kivy/buildozer).
2. Run `buildozer init` and edit the `buildozer.spec` file as needed.
3. Build the APK:
   ```bash
   buildozer -v android debug
   ```

## License

This project is licensed under the MIT License.
