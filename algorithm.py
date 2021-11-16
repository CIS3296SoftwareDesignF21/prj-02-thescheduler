def sift_sections(courses):
    ret_schedule = {}

    conflict = False

    for current_course_listing, current_course in courses.items():
        # print("course: " + str(current_course))
        # print("length of course: " + str(len(current_course)))
        # print("type of course: " + str(type(current_course)))
        for current_section in current_course.get("sections"):
            # print("section: " + str(current_section))
            # print("length of section: " + str(len(current_section)))
            # print("type of section: " + str(type(current_section)))
            current_section_num = current_section[0]
            # print("current_section_num: " + current_section_num)
            for current_meeting in current_section[1]:
                # print("current_meeting: " + str(current_meeting))
                current_meeting_day = current_meeting.get("day")
                current_meeting_start = current_meeting.get("start")
                current_meeting_end = current_meeting.get("end")

                for selected_course in ret_schedule.values():
                    for current_selected_meeting in selected_course.get("meetings"):
                        if current_meeting_day == current_selected_meeting.get("day"):
                            if current_meeting_start >= current_selected_meeting.get("start"):
                                if current_meeting_end <= current_selected_meeting.get("end"):
                                    conflict = True
            if not conflict:
                new_listing = {
                    "credits": current_course.get("credits"),
                    "section": current_section[0],
                    "meetings": []
                }

                for current_meeting in current_section[1]:
                    new_listing.get("meetings").append({
                        "day": current_meeting.get("day"),
                        "start": current_meeting.get("start"),
                        "end": current_meeting.get("end"),
                        "instructor": current_meeting.get("instructor")
                    })

                ret_schedule[current_course_listing] = new_listing
                # print("ret_schedule: " + str(ret_schedule))

            else:
                conflict = False

    return ret_schedule


sample_courses = {
    "course1": {
        "credits": "4",
        "sections": [
            ("1", [
                {
                    "day": "monday",
                    "start": "9:00",
                    "end": "9:50",
                    "instructor": "Professor Plum"
                },
                {
                    "day": "tuesday",
                    "start": "13:00",
                    "end": "14:50",
                    "instructor": "TA Tim"
                },
                {
                    "day": "wednesday",
                    "start": "9:00",
                    "end": "9:50",
                    "instructor": "Professor Plum"
                }
            ]),
            ("2", [
                {
                    "day": "monday",
                    "start": "10:00",
                    "end": "10:50",
                    "instructor": "Professor Plum"
                },
                {
                    "day": "tuesday",
                    "start": "14:00",
                    "end": "15:50",
                    "instructor": "TA Tim"
                },
                {
                    "day": "wednesday",
                    "start": "10:00",
                    "end": "10:50",
                    "instructor": "Professor Plum"
                }
            ])
        ],
    },
    "course2": {
        "credits": "3",
        "sections": [
            ("1", [
                {
                    "day": "tuesday",
                    "start": "13:00",
                    "end": "13:50",
                    "instructor": "Instructor Ian"
                },
                {
                    "day": "wednesday",
                    "start": "10:00",
                    "end": "11:50",
                    "instructor": "TA Thomas"
                },
                {
                    "day": "thursday",
                    "start": "13:00",
                    "end": "13:50",
                    "instructor": "Instructor Ian"
                }
            ]),
            ("2", [
                {
                    "day": "tuesday",
                    "start": "12:00",
                    "end": "12:50",
                    "instructor": "Instructor Ian"
                },
                {
                    "day": "wednesday",
                    "start": "10:00",
                    "end": "11:50",
                    "instructor": "TA Thomas"
                },
                {
                    "day": "thursday",
                    "start": "12:00",
                    "end": "12:50",
                    "instructor": "Instructor Ian"
                }
            ])
        ]
    }
}

print("\noutput: " + str(sift_sections(sample_courses)))
