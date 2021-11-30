def sift_sections(courses):
    input_courses = courses.copy()

    ret_schedules = {}

    proposed_schedule = {}

    conflict = False

    i = 1

    last_good_section_num = 0

    while True:
        for current_course_listing, current_course in input_courses.items():
            print("course: " + str(current_course_listing))
            # print("length of course: " + str(len(current_course)))
            # print("type of course: " + str(type(current_course)))
            if len(current_course.get("sections")) == 0:
                return ret_schedules
            for current_section_num, meetings in current_course.get("sections").items():
                print(current_course_listing + " section: " + str(current_section_num) + " meetings: " + str(meetings))
                # print("length of section: " + str(len(meetings)))
                # print("type of section: " + str(type(meetings)))
                # print("current_section_num: " + current_section_num)
                if len(proposed_schedule) >= 1:
                    if current_course_listing in proposed_schedule.keys():
                        conflict = True
                        print("Conflict: repeat course")
                if not conflict:
                    for current_meeting in meetings:
                        # print("current_meeting: " + str(current_meeting))
                        current_meeting_day = current_meeting.get("day")
                        current_meeting_start = current_meeting.get("start")
                        current_meeting_end = current_meeting.get("end")

                        if len(proposed_schedule) >= 1:
                            # repeat course
                            if current_course_listing in proposed_schedule.keys():
                                conflict = True
                                print("Conflict: repeat course")
                            else:
                                for selected_course in proposed_schedule.values():
                                    for current_selected_meeting in selected_course.get("meetings"):
                                        if current_meeting_day == current_selected_meeting.get("day"):

                                            # new meeting encapsulates proposed meeting
                                            if current_meeting_start >= current_selected_meeting.get("start"):
                                                if current_meeting_end <= current_selected_meeting.get("end"):
                                                    conflict = True
                                                    print("Conflict: new meeting encapsulates proposed meeting")

                                            # proposed meeting clips beginning of existing meeting
                                            if current_meeting_start >= current_selected_meeting.get("start"):
                                                if current_meeting_end <= current_selected_meeting.get("start"):
                                                    conflict = True
                                                    print("Conflict: new meeting clips beginning of proposed meeting")

                                            # proposed meeting clips end of existing meeting
                                            if current_meeting_start >= current_selected_meeting.get("end"):
                                                if current_meeting_end <= current_selected_meeting.get("end"):
                                                    conflict = True
                                                    print("Conflict: new meeting clips end of proposed meeting")

                    if not conflict:
                        new_listing = {
                                "credits": current_course.get("credits"),
                                "section": current_section_num,
                                "meetings": []
                            }

                        last_good_section_num = current_section_num
                        print(current_course_listing + " section " + current_section_num + " is good")

                        for current_meeting in meetings:
                            new_listing.get("meetings").append({
                                "day": current_meeting.get("day"),
                                "start": current_meeting.get("start"),
                                "end": current_meeting.get("end"),
                                "instructor": current_meeting.get("instructor")
                            })
                        # print(new_listing)

                        proposed_schedule[current_course_listing] = new_listing

                    else:
                        conflict = False

                else:
                    conflict = False
        print("New proposed schedule " + str(i) + " " + str(proposed_schedule))
        if len(proposed_schedule) == len(input_courses):
            ret_schedules[i] = proposed_schedule
            proposed_schedule = {}
            input_courses.get(current_course_listing).get("sections").pop(last_good_section_num)
            i += 1
            # print("ret_schedules: " + str(ret_schedules))
        else:
            return ret_schedules


sample_courses = {
    "course1": {
        "credits": "4",
        "sections": {
            "1": [
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
            ],
            "2": [
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
            ]
        },
    },
    "course2": {
        "credits": "3",
        "sections": {
            "1": [
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
            ],
            "2": [
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
            ],
            "3": [
                {
                    "day": "tuesday",
                    "start": "8:00",
                    "end": "8:50",
                    "instructor": "Instructor Ian"
                },
                {
                    "day": "wednesday",
                    "start": "12:00",
                    "end": "13:50",
                    "instructor ": "TA Thomas"
                },
                {
                    "day": "thursday",
                    "start": "8:00",
                    "end": "8:50",
                    "instructor": "Instructor Ian"
                }
            ]
        }
    }
}

print("\noutput: " + str(sift_sections(sample_courses)))
