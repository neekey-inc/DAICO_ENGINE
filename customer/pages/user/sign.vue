<template>
  <el-row :getter="20">
    <el-col :sm="10">
      <h2>マイアカウントを登録済みのお客様</h2>
      <el-form>
          <el-form-item label="メールアドレス">
              <el-input placeholder="メールアドレス" name="email"></el-input>
          </el-form-item>
          <el-form-item label="パスワード">
              <el-input type="password" placeholder="パスワード" name="password"></el-input>
          </el-form-item>
          <el-form-item>
              <el-button @click="onSubmit">ログイン</el-button>
          </el-form-item>
          <a><el-link>パスワードをお忘れの方</el-link></a>
      </el-form>
    </el-col>
    <el-col :sm="10">
      <h2>ログイン・マイアカウント登録</h2>
      <el-form class="body" ref="form">
          <el-form-item label="お名前">
              <el-input placeholder="お名前"></el-input>
          </el-form-item>
          <el-form-item label="メールアドレス">
              <el-input placeholder="メールアドレス"></el-input>
          </el-form-item>
          <el-form-item label="パスワード">
              <el-input type="password" placeholder="パスワード"></el-input>
          </el-form-item>
          <el-form-item label="パスワード確認">
              <el-input type="password" placeholder="もう一度パスワードを入力してください"></el-input>
          </el-form-item>
          <el-form-item>
              <el-button @click="onSubmit">会員登録</el-button>
          </el-form-item>
          ボタンを押すと利用規約に同意したことになります
      </el-form>
    </el-col>
  </el-row>







</template>
