from plyer import notification

title='Your NITIN'
message='Have a nice day '

notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    toast=False)
