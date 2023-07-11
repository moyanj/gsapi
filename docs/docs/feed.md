<style>
    #mo-feedback-form {
        margin: 20px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #f9f9f9;
    }
        
        /* 示例：标题样式 */
        .mo-title {
            font-size: 24px;
            font-weight: bold;
            color: #333;
        }
        
        /* 示例：输入框样式 */
        .mo-input {
            width: 300px;
            height: 30px;
            margin-bottom: 10px;
            padding: 5px;
            border: 1px solid #ddd;
            border-radius: 3px;
        }
        
        /* 示例：文本框样式 */
        .mo-textarea {
            width: 300px;
            height: 100px;
            margin-bottom: 10px;
            padding: 5px;
            border: 1px solid #ddd;
            border-radius: 3px;
        }
        
        /* 示例：提交按钮样式 */
        .mo-submit-btn {
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
</style>
<div id="mo-feedback-form">
    <h1 class="mo-title">用户反馈</h1>
            <label for="name">您的姓名：</label>
            <input type="text" id="name" name="name" class="mo-input" required><br><br>
            
            <label for="email">您的邮箱：</label>
            <input type="email" id="email" name="email" class="mo-input" required><br><br>
            
            <label for="message">反馈信息：</label><br>
            <textarea id="message" name="message" class="mo-textarea" required></textarea><br><br>
            
            <input type="button" id = "mo-upload"value="提交反馈" class="mo-submit-btn">
        <script>
            function event1(){
                var name = $("#name").val() 
                var mail = $("#email").val()
                var ms = $("#message").val()
	            $.get("https://gsapi.moyanjdc.top/feed.php",{"name":name,"email":mail,"message":ms})
	            alert("提交成功")
            }
            $("#mo-upload").bind("click",event1);
        </script>
</div>