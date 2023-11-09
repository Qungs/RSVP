## Initial RVSP

import openai
import tkinter as tk
from tkinter import font

# Assuming you've set your OpenAI API key in your environment variables for security reasons
openai.api_key = "your-api-key"


# Function to send data to the ChatGPT API and receive a response
def get_chatgpt_response(user_input, text_widget):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or the appropriate model you want to use
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": user_input}]
        )
        display_text = response.choices[0].message['content']
        start_rsvp_display(display_text, text_widget)
    except openai.error.OpenAIError as e:
        text_widget.config(state=tk.NORMAL)
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, f"An error occurred: {e}")
        text_widget.config(state=tk.DISABLED)

# Function to update the text box with words from the response
def update_text_box(text_widget, words, index, delay):
    if index < len(words):
        word = words[index]
        text_widget.config(state=tk.NORMAL)
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, word)
        text_widget.tag_configure("center", justify='center')
        text_widget.tag_add("center", "1.0", "end")
        text_widget.config(state=tk.DISABLED)
        index += 1
        # Schedule the next update
        text_widget.after(delay, update_text_box, text_widget, words, index, delay)

# Function to start the RSVP display
def start_rsvp_display(text, text_widget):
    words = text.split()
    wpm = speed_scale.get()
    delay = int((60 / wpm) * 1000)  # Delay in milliseconds
    update_text_box(text_widget, words, 0, delay)

# Main function to set up the Tkinter window
def main():
    global speed_scale
    root = tk.Tk()
    root.title("ChatGPT with RSVP Reader")

    # Define the main font style
    main_font = font.Font(family="Helvetica", size=24)

    # Input box
    user_input = tk.Entry(root, font=main_font)
    user_input.pack(fill=tk.X, padx=10, pady=10)

    # RSVP Text widget
    text_widget = tk.Text(root, height=1, width=20, font=main_font, bg="black", fg="white")
    text_widget.pack(padx=10, pady=(0, 10))
    text_widget.tag_configure("center", justify='center')
    text_widget.tag_add("center", "1.0", "end")
    text_widget.config(state=tk.DISABLED)

    # Speed control scale
    speed_scale = tk.Scale(root, from_=100, to=1000, orient=tk.HORIZONTAL, label="Words per Minute (WPM)")
    speed_scale.pack(fill=tk.X, padx=10)

    # Submit button
    submit_button = tk.Button(root, text="Submit", font=main_font, command=lambda: get_chatgpt_response(user_input.get(), text_widget))
    submit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
