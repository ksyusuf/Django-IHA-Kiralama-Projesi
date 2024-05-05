<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script type="text/javascript">
    $(document).ready(function() {
        $(".cancel-btn").click(function() {
            var obj_id = $(this).data("data-obj-id");
            $.ajax({
                url: "/rent_delete/",
                method: "POST",
                data: {
                    obj_id: obj_id,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function(data) {
                    // İşlem başarılı olduğunda yapılacak işlemler
                    alert("İptal işlemi başarılı.");
                    // Gerekirse sayfayı yenileyebilirsiniz.
                    // window.location.reload();
                },
                error: function(xhr, errmsg, err) {
                    // Hata durumunda yapılacak işlemler
                    console.log(xhr.status + ": " + xhr.responseText);
                    alert("İptal işlemi sırasında bir hata oluştu.");
                }
            });
        });
    });
</script>