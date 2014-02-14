from django.db.models import *


notify = False

class Post(BaseModel):
    title = CharField(max_length=60)
    body = TextField()
    created = DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
	return self.title


class Comment(BaseModel):
    author = CharField(max_length=60, blank=True)
    body = TextField()
    post = ForeignKey(Post, related_name="comments", blank=True, null=True)
    created = DateTimeField(auto_now_add=True)

    def __unicode__(self):
	return u"%s: %s" % (self.post, self.body[:60])

    def save(self, *args, **kwargs):
	"""Email when a comment is added."""
	if notify:
	    tpl = "Comment was added to '%s' by '%s': \n\n%s"
	    message = tp1 % (self.post, self.author, self.body)
	    from_addr = "no-reply@jeremyredd.com"
	    recipient_list = ["contact@jeremyredd.com"]

	    send_mail("New comment added", message, from_addr, recipient_list)
	super(Comment, self).save(*args, **kwargs)
