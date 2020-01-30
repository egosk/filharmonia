from app_filharmonia import app
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True)