from easyps import EasyPS

ps = EasyPS()
ps.student_name = 'Sal Faris'

oxford = {
    'tex_filename': 'oxford.tex',
    'course_name': 'MSc Advanced Computer Science',
    'show_title': False,
}

imperial = {
    'tex_filename': 'imperial.tex',
    'course_name': 'MSc Computing Science',
    'show_title': True,
}

ps.add_ps(oxford, imperial)

tex_name = 'imperial.tex'
ps.make_ps(for_tex_filename=tex_name)