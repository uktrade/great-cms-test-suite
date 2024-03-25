from behave import given, then, when

from tests.behavioural.pages.export_academy.events_page import ExportAcademyEventsPage


@given(u'I am in export academy events page and logged in')
def step_impl(context):
    ukea_events_page = ExportAcademyEventsPage(context)
    ukea_events_page.get_url()
    assert context.browser.current_url == ukea_events_page.url


@when(u'I click on an event')
def step_click_event(context):
    ukea_events_page = ExportAcademyEventsPage(context)
    ukea_events_page.get_url()
    assert context.browser.current_url == ukea_events_page.url
    ukea_events_page.visit_an_event_detail_page()

    assert context.browser.current_url.split('/')[-2].split('-')[0] in ukea_events_page.event_title().lower()


@then(u'I should see details of that event')
def step_see_event_details(context):
    ukea_events_page = ExportAcademyEventsPage(context)
    ukea_events_page.get_url()
    ukea_events_page.visit_an_event_detail_page()
    assert ukea_events_page.is_event_detail_visible() is True
