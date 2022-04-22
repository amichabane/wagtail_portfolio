from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroText(blocks.StructBlock):
    title = blocks.RichTextBlock(default="Title", required=False)
    description = blocks.RichTextBlock(default="Description", required=False)
    image = ImageChooserBlock()

    class Meta:
        template = 'myportfolio/hero_text.html'
        icon = 'user'


class PortfolioBlock(blocks.StructBlock):
    title = blocks.CharBlock(default="Title", required=False)
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("title", blocks.CharBlock()),
                ("text", blocks.TextBlock(required=False, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False,
                                               help_text="If the button page above is selected, that will be used first.")),
            ]
        )
    )

    class Meta:
        template = 'myportfolio/Portfolio.html'
        icon = 'image'


class blockabout(blocks.StructBlock):
    title = blocks.RichTextBlock(default="Title", required=False)
    abouts = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("description", blocks.RichTextBlock(required=False)),
                ("text", blocks.RichTextBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = 'myportfolio/bio.html'
        icon = 'user'


class skillsblock(blocks.StructBlock):
    title = blocks.RichTextBlock(default="Title", required=False)
    text = blocks.RichTextBlock(required=False)
    skills = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("subtitle", blocks.CharBlock(required=False)),
                ("description", blocks.RichTextBlock(required=False)),
            ]
        )
    )

    class Meta:
        template = 'myportfolio/skill.html'
        icon = "Placeholder"
