(function ($) {
    $(document).ready(function () {
        $('#id_Course').change(function () {
            var CourseId = $(this).val();
            $.ajax({
                type: 'GET',
                url: '/admin/MyApp1/teacher/add/',
                data: {
                    Course_id: CourseId
                },
                success: function (data) {
                    var classesField = $('#id_classes');
                    classesField.empty();
                    $.each(data.classes, function (index, value) {
                        classesField.append($('<option></option>').attr('value', value.id).text(value.name));
                    });
                }
            });
        });
    });
})(django.jQuery);