from pyeasyps.pyeasyps import EasyPS, University

oxford = University(
    tex_filename='oxford.tex',
    course_name='MSc Advanced Computer Science', 
    show_title=False)

imperial = University(
    tex_filename='imperial.tex',
    course_name='MSc Computing Science', 
    show_title=True)

if __name__ == '__main__':
    doc = EasyPS(content_dir='./content', student_name='Salman Faris')
    target_uni = [oxford, imperial]
    doc.generate_ps(target_uni)