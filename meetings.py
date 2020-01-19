def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)
    # return sorted_meetings

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for meeting_start, meeting_end in sorted_meetings[1:]:

        last_meeting_start, last_meeting_end = merged_meetings[-1]
        if(meeting_start <= last_meeting_end):
            merged_meetings[-1] = (last_meeting_start,
                                   max(last_meeting_end, meeting_end))
        else:
            merged_meetings.append((meeting_start, meeting_end))

    return merged_meetings


print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))


# O(nlg(n)) time, O(1) space
