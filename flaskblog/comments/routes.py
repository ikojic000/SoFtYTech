from flask import Blueprint, redirect, render_template, flash, url_for, request
from flask.json import jsonify
from flask_login import login_required
from flask_user import roles_required
from flaskblog.comments.database_manager import (
    count_comments,
    delete_all_users_comments,
    delete_comment_by_id,
    get_all_comments,
)
from flaskblog.comments.utils import get_comments_count
from flaskblog.logs.request_logging import after_request, before_request

# Create a Blueprint for managing comments
comments = Blueprint("comments", __name__)

# Register before and after request handlers for logging
comments.before_request(before_request)
comments.after_request(after_request)


# Dashboard - Table with all comments with edit/delete buttons
@comments.route("/admin/comments/all")
@login_required
@roles_required(["Admin", "Superadmin"])
def all_comments():
    """
    Display all comments in a table with edit/delete buttons.

    Returns:
        render_template: Renders the admin-comments.html template.
    """
    title = "All Comments"
    comments_data = get_all_comments()

    context = {"pageTitle": title, "comments": comments_data}

    return render_template("admin/admin-comments.html", **context)


# Deleting Comments - New Design
@comments.route("/admin/comments/delete/<int:comment_id>")
@login_required
@roles_required(["Admin", "Superadmin"])
def delete_comment(comment_id):
    """
    Delete a comment by its ID.

    Args:
        comment_id (int): The ID of the comment to be deleted.

    Returns:
        redirect: Redirects back to the referring page or a default page.
    """
    delete_comment_by_id(comment_id)
    flash("You have deleted the comment!", "success")

    # Get the referrer (URL that the request came from)
    referrer = request.referrer

    # If the referrer is None (e.g., direct access to the delete URL),
    # then redirect to a default page
    if referrer is None:
        return redirect(url_for("posts.allComments"))

    # Otherwise, redirect back to the referrer
    return redirect(referrer)


# Route to delete all comments by a specific user
@comments.route("/admin/comments/delete/user/<int:user_id>")
@login_required
@roles_required(["Admin", "Superadmin"])
def delete_all_comments_by_user(user_id):
    """
    Delete all comments by a specific user.

    Args:
        user_id (int): The ID of the user whose comments should be deleted.

    Returns:
        redirect: Redirects to the user details page after deleting comments.
    """
    delete_all_users_comments(user_id)

    return redirect(url_for("users.user_details", user_id=user_id))


# Method that returns the total number of comments
@comments.route("/api/comments/number_of_comments", methods=["GET"])
def number_of_comments():
    """
    Return the total number of comments.

    Returns:
        jsonify: JSON response containing the number of comments.
    """
    number_of_comments_data = count_comments()
    return jsonify(number_of_comments=number_of_comments_data)


# Method that returns list of number of comments per month
@comments.route("/api/comments/count_by_months", methods=["GET"])
def comment_count():
    """
    Return the count of comments in each month.

    Returns:
        jsonify: JSON response containing comment counts for each month.
    """
    comment_count_list = []

    for x in range(1, 13):
        comment_count_list.append(get_comments_count(x))

    return jsonify(commentCountList=comment_count_list)
