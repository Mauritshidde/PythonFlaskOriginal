from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlite3, json, collections, sys, os

def aantal_taxis2(aantal, groottes):
    num_een, num_twee, num_drie, num_taxi = 0, 0, 0, 0
    for grootte in groottes:
        if grootte == 4:
            num_taxi += 1
        elif grootte == 3:
            num_drie += 1
        elif grootte == 2:
            num_twee += 1
        elif grootte == 1:
            num_een += 1

    num_taxi += num_drie
    num_een -= num_drie

    num_taxi += num_twee//2

    rest_twee = num_twee%2
    num_taxi += rest_twee

    if rest_twee > 0:
        num_een -= 2

    if num_een > 0:
        num_taxi += math.ceil(num_een // 4)

    print(num_taxi)
