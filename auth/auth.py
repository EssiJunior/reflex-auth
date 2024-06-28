"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...
class FormState(rx.State):

    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        "Handle the form submit."
        self.form_data = form_data

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.form(
                rx.vstack(
                    rx.heading("Sign In", size="9", style={'margin': '0 auto'}),
                    rx.hstack(
                        rx.text("Email", 
                            style={
                                'font-size': '0.75rem',
                                'width': '100%',
                                'margin': '0',
                                'font-weight': '600',
                                # 'background': 'white',
                            }
                        ),
                        rx.input(
                            placeholder="Enter your email address",
                            id="email",
                            style={
                                'width': '100%',
                                'margin': '0.25rem 0',
                            }
                        ),
                        style={
                            'margin': '2rem auto 0.5rem auto',
                            # 'background': 'brown',
                            'width': '50%',
                            'display': 'flex',
                            'flexDirection': 'column',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'gap':'0',
                            
                        }
                    ),
                    rx.hstack(
                        rx.text("Password", 
                            style={
                                'font-size': '0.75rem',
                                'width': '100%',
                                'margin': '0',
                                'font-weight': '600',
                                # 'background': 'white',
                            }
                        ),
                        rx.input(
                            placeholder="Enter your passord",
                            id="password",
                            type='password',
                            style={
                                'width': '100%',
                                'margin': '0.25rem 0',
                            }
                        ),
                        style={
                            'margin': '0.5rem auto 2rem auto',
                            # 'background': 'brown',
                            'width': '50%',
                            'display': 'flex',
                            'flexDirection': 'column',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'gap':'0',
                            
                        }
                    ),
                    rx.button("Submit", 
                            type_="submit", 
                            border_radius="lg",
                            background_image="linear-gradient(144deg,orange,red 50%,orangered)",
                            style={
                                'margin': 'auto',
                                # 'background': 'orange',
                                'width': '50%',
                                'display': 'flex',
                                'flexDirection': 'column',
                                'justifyContent': 'center',
                                'alignItems': 'center',
                                'gap':'0',
                                'cursor': 'pointer',
                                
                            },
                            opacity=1,
                            _hover={
                                "opacity": 0.7,
                            },
                    ),
                    # rx.input(
                    #     placeholder="Last Name", id="last_name"
                    # ),
                    # rx.hstack(
                    #     rx.checkbox("Checked", id="check"),
                    #     rx.switch("Switched", id="switch"),
                    # ),
                ),
                # background_color='red',
                margin_top="5rem",
                align="center",
                justify="center",
                on_submit=FormState.handle_submit,
            ),
            rx.divider(),
            rx.hstack(
                rx.heading("Results"),
                rx.text(FormState.form_data.to_string()),
                bg='skyblue',
                color='black',
                style={'padding':'0.25rem 1rem'}
            ),
            width="70%",
            spacing="5",
            min_height="85vh",
            margin='auto',
            # background_color='green',
            style={
                'display':'flex',
                'flexDirection':'column',
                'justifyContent':'center',
                'alignItems':'center',
                'gap':'1rem',
                'padding':'1rem',
            }
            
        ),
        # rx.vstack(
        #     rx.heading("Welcome to Reflex!", size="9"),
        #     rx.text(
        #         "Get started by editing ",
        #         rx.code(f"{config.app_name}/{config.app_name}.py"),
        #         size="5",
        #     ),
        #     rx.link(
        #         rx.button("Check out our docs!"),
        #         href="https://reflex.dev/docs/getting-started/introduction/",
        #         is_external=True,
        #     ),
        #     spacing="5",
        #     justify="center",
        #     min_height="85vh",
        #     background_color='RED'
        # ),
        rx.logo(),
        # background_color='yellow',
    )


app = rx.App()
app.add_page(index)
