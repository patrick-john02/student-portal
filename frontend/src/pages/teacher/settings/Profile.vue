<script lang="ts">
export const description = "Teacher profile settings page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"

import { User, Camera } from "lucide-vue-next"

const userRole = "Teacher"

// Profile states
const avatar = ref<File | null>(null)
const firstName = ref("Juan")
const lastName = ref("Dela Cruz")
const email = ref("juan.delacruz@example.com")
const contact = ref("09123456789")

// Password change
const currentPassword = ref("")
const newPassword = ref("")
const confirmPassword = ref("")

function handleAvatarUpload(e: Event) {
  const target = e.target as HTMLInputElement
  if (target.files?.length) {
    avatar.value = target.files[0]
  }
}
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- PAGE HEADER -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Profile Settings</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- CONTENT -->
      <div class="p-4 flex flex-col gap-6 pb-10">
        <h2 class="text-2xl font-bold tracking-tight">Profile Settings</h2>
        <p class="text-sm text-muted-foreground">
          Manage your personal information, account details, and security settings.
        </p>

        <!-- PROFILE INFORMATION -->
        <Card>
          <CardHeader>
            <CardTitle>Personal Information</CardTitle>
            <CardDescription>Update your basic profile details.</CardDescription>
          </CardHeader>

          <CardContent class="space-y-6">
            <!-- AVATAR UPLOAD -->
            <div class="flex items-center gap-6">
              <Avatar class="h-20 w-20">
                <AvatarImage
                  v-if="avatar"
                  :src="URL.createObjectURL(avatar)"
                />
                <AvatarFallback>
                  <User class="h-8 w-8 text-muted-foreground" />
                </AvatarFallback>
              </Avatar>

              <div>
                <Label for="avatarUpload" class="cursor-pointer">
                  <div
                    class="flex items-center gap-2 text-sm font-medium hover:text-primary transition"
                  >
                    <Camera class="h-4 w-4" />
                    Change Profile Photo
                  </div>
                </Label>

                <Input
                  id="avatarUpload"
                  type="file"
                  class="hidden"
                  @change="handleAvatarUpload"
                />
              </div>
            </div>

            <!-- GRID FORM -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="grid gap-2">
                <Label>First Name</Label>
                <Input v-model="firstName" />
              </div>

              <div class="grid gap-2">
                <Label>Last Name</Label>
                <Input v-model="lastName" />
              </div>

              <div class="grid gap-2">
                <Label>Email</Label>
                <Input v-model="email" disabled class="bg-muted" />
              </div>

              <div class="grid gap-2">
                <Label>Contact Number</Label>
                <Input v-model="contact" />
              </div>
            </div>
          </CardContent>

          <CardFooter class="flex justify-end">
            <Button class="gap-2">Save Changes</Button>
          </CardFooter>
        </Card>

        <!-- PASSWORD SETTINGS -->
        <Card>
          <CardHeader>
            <CardTitle>Password & Security</CardTitle>
            <CardDescription>Update your password regularly for security.</CardDescription>
          </CardHeader>

          <CardContent class="space-y-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="grid gap-2">
                <Label>Current Password</Label>
                <Input type="password" v-model="currentPassword" />
              </div>

              <div class="grid gap-2">
                <Label>New Password</Label>
                <Input type="password" v-model="newPassword" />
              </div>

              <div class="grid gap-2">
                <Label>Confirm Password</Label>
                <Input type="password" v-model="confirmPassword" />
              </div>
            </div>
          </CardContent>

          <CardFooter class="flex justify-end">
            <Button variant="secondary">Update Password</Button>
          </CardFooter>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
