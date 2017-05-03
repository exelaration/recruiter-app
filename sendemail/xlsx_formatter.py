from events.models import Event, Attendance

import io
import xlsxwriter


def writeToExcel(attendance_list, event):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)

    # Here we will adding the code to add data
    worksheet_s = workbook.add_worksheet("Summary")
    title = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    cell = workbook.add_format({
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    title_text = "{0} {1}".format("Attendance for", event.title)
    worksheet_s.merge_range('A2:E2', title_text, title)
    worksheet_s.write(3, 0, "", header)
    worksheet_s.write(3, 1, "First Name", header)
    worksheet_s.write(3, 2, "Last Name", header)
    worksheet_s.write(3, 3, "Email", header)
    worksheet_s.write(3, 4, "Phone", header)
    worksheet_s.write(3, 5, "Selected Job Posting", header)

    for idx, data in enumerate(attendance_list):
        row = 4 + idx
        row_number = str(idx + 1)
        worksheet_s.write_string(row, 0, row_number, cell)
        worksheet_s.set_column(1, 1, width=20)
        worksheet_s.write_string(row, 1, data.candidate.first_name, cell)
        worksheet_s.set_column(2, 2, width=20)
        worksheet_s.write_string(row, 2, data.candidate.last_name, cell)
        worksheet_s.set_column(3, 3, width=35)
        worksheet_s.write_string(row, 3, str(data.candidate.email), cell)
        worksheet_s.set_column(4, 4, width=20)
        worksheet_s.write_string(row, 4, str(data.candidate.phone), cell)
        worksheet_s.set_column(5, 5, width=60)
        worksheet_s.write_string(row, 5, str(data.selected_job_posting), cell)

    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data