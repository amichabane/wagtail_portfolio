from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.core.fields import StreamField, RichTextField

from wagtail.core.models import Page

from myportfolio.blocks import HeroText,PortfolioBlock,blockabout,skillsblock


class HomePage(Page):

        body=StreamField([
            ('HeroText',HeroText()),
            ('Portfolio',PortfolioBlock()),
            ('Bio',blockabout()),
            ('skill',skillsblock())

        ],null=True)
        content_panels =Page.content_panels+[
                StreamFieldPanel('body')
        ]


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm):

    template = "myportfolio/contact_page.html"
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "myportfolio/contact_page_landing.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]