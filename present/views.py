from flask import render_template, redirect, url_for, flash
from present import app, db
from present.models import User, Present, PastRecord
from present.forms import addPresent, BinggoPresent
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.sql import func
import datetime


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        past_record = PastRecord.query.all()
    except OperationalError:
        past_record = None

    pre_record = PastRecord.query.order_by(PastRecord.name.desc()).first()
    if pre_record:
        time_diff = datetime.datetime.now() - pre_record.timestamp
        print(time_diff.total_seconds(), pre_record.timestamp, datetime.datetime.now())

        if time_diff.total_seconds() > 100:
            pre_record.state = True
            db.session.commit()
    return render_template("index.html", past_record=past_record)
    # past_record = PastRecord.query.order_by(PastRecord.name).first()
    # presents = Present.query.with_parent(past_record).all()

    # form = addPresent()
    # if form.validate_on_submit():
    #     if len(presents) > 10:
    #         flash("每期最多有10个礼物", "warning")
    #         return redirect(url_for("index"))
    #     else:
    #         name = form.present_name.data
    #         present = Present(name=name, past_id=past_record.name)
    #         db.session.add(present)
    #         try:
    #             db.session.commit()
    #             flash("礼物创建成功.", "success")
    #         except IntegrityError:
    #             flash("礼物不能重复", "danger")
    #         return redirect(url_for("index"))

    # return render_template(
    #     "index.html", past_record=past_record, form=form, presents=presents
    # )


@app.route("/present/edit/<int:present_id>", methods=["GET", "POST"])
def edit(present_id):
    present = Present.query.get_or_404(present_id)
    form = addPresent()
    if form.validate_on_submit():
        name = form.present_name.data
        present.present_name = name
        db.session.commit()
        flash("Item updated")
        return redirect(url_for("index"))
    return render_template("edit.html", present=present)

    return redirect("index.html")


@app.route("/show_page/<int:page_id>", methods=["GET", "POST"])
def show_page(page_id):
    record = PastRecord.query.filter_by(name=page_id).first()
    if record == None:
        past_record = PastRecord(name=page_id)
        db.session.add(past_record)
        db.session.commit()
        if past_record.name == 1:
            past_record.state = True
            db.session.add(past_record)
            db.session.commit()
        return redirect(url_for("index"))
    else:
        past_record = record

    presents = Present.query.with_parent(past_record).all()
    binggo_form = BinggoPresent()
    form = addPresent()
    if form.validate_on_submit():
        if len(presents) > 10:
            flash("每期最多有10个礼物", "warning")
            return redirect(url_for(".show_page"))
        else:
            name = form.present_name.data
            present = Present(name=name, past_id=page_id)
            db.session.add(present)
            try:
                db.session.commit()
                flash("礼物创建成功.", "success")
            except IntegrityError:
                flash("礼物不能重复", "danger")
            return redirect(url_for(".show_page", page_id=page_id))

    print(binggo_form.data)
    if binggo_form.validate_on_submit():
        print(binggo_form.data)
        past_record.binggo_name = binggo_form.binggo_name.data
        db.session.commit()

    return render_template(
        "present_list.html",
        presents=presents,
        form=form,
        past_record=past_record,
        binggo_form=binggo_form,
    )
