"""  # lint-amnesty, pylint: disable=django-not-configured
Contains configuration for schedules app
"""


from edx_toggles.toggles import (
    WaffleFlag,
    LegacyWaffleFlagNamespace,
    LegacyWaffleSwitch,
    LegacyWaffleSwitchNamespace
)

from openedx.core.djangoapps.waffle_utils import CourseWaffleFlag

WAFFLE_FLAG_NAMESPACE = LegacyWaffleFlagNamespace(name='schedules')
WAFFLE_SWITCH_NAMESPACE = LegacyWaffleSwitchNamespace(name='schedules')

CREATE_SCHEDULE_WAFFLE_FLAG = CourseWaffleFlag(
    waffle_namespace=WAFFLE_FLAG_NAMESPACE,
    flag_name='create_schedules_for_course',
    module_name=__name__,
)

COURSE_UPDATE_WAFFLE_FLAG = CourseWaffleFlag(
    waffle_namespace=WAFFLE_FLAG_NAMESPACE,
    flag_name='send_updates_for_course',
    module_name=__name__,
)

# .. toggle_name: schedules.enable_debugging
# .. toggle_implementation: WaffleFlag
# .. toggle_default: False
# .. toggle_description: Enable debug level of logging for schedules messages.
# .. toggle_use_cases: open_edx
# .. toggle_creation_date: 2017-09-17
DEBUG_MESSAGE_WAFFLE_FLAG = WaffleFlag('schedules.enable_debugging', __name__)

COURSE_UPDATE_SHOW_UNSUBSCRIBE_WAFFLE_SWITCH = LegacyWaffleSwitch(
    WAFFLE_SWITCH_NAMESPACE,
    'course_update_show_unsubscribe',
    __name__
)
