<script lang="ts">
export const description = "Teacher subjects page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import {ref} from 'vue'
import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
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
} from "@/components/ui/card"

import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  Users,
  MoreHorizontal,
} from "lucide-vue-next"

const userRole = "Teacher"

const search = ref("")

// Dummy subjects assigned to the teacher
const subjects = ref([
  {
    id: 1,
    name: "General Mathematics",
    code: "MATH-11",
    grade: "Grade 11",
    students: 45,
    color: "bg-blue-500",
  },
  {
    id: 2,
    name: "Oral Communication",
    code: "ENG-11",
    grade: "Grade 11",
    students: 38,
    color: "bg-green-500",
  },
  {
    id: 3,
    name: "Earth & Life Science",
    code: "SCI-11",
    grade: "Grade 11",
    students: 40,
    color: "bg-purple-500",
  },
  {
    id: 4,
    name: "Physical Education",
    code: "PE-12",
    grade: "Grade 12",
    students: 42,
    color: "bg-red-500",
  },
])
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Subjects</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Page Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        
        <!-- Page Header -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">My Subjects</h2>
            <p class="text-sm text-muted-foreground">
              View your assigned subjects and manage class content.
            </p>
          </div>
        </div>

        <!-- Subjects Table -->
        <Card>
          <CardHeader>
            <CardTitle>Subjects Overview</CardTitle>
            <CardDescription>
              These are the subjects assigned to your teaching load.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <!-- Search -->
            <div class="flex justify-between mb-4">
              <Input
                v-model="search"
                placeholder="Search subjects..."
                class="max-w-xs"
              />
            </div>

            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-64">Subject</TableHead>
                  <TableHead>Grade Level</TableHead>
                  <TableHead class="text-center">Students</TableHead>
                  <TableHead class="text-right w-20">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="sub in subjects"
                  :key="sub.id"
                  class="hover:bg-muted/50 transition-colors"
                >
                  <!-- Subject Info -->
                  <TableCell>
                    <div class="flex items-center gap-2">
                      <div class="h-3 w-3 rounded-full" :class="sub.color"></div>
                      <div>
                        <p class="font-medium">{{ sub.name }}</p>
                        <p class="text-xs text-muted-foreground">{{ sub.code }}</p>
                      </div>
                    </div>
                  </TableCell>

                  <!-- Grade Level -->
                  <TableCell>
                    <Badge variant="secondary">{{ sub.grade }}</Badge>
                  </TableCell>

                  <!-- Students Count -->
                  <TableCell class="text-center">
                    <Badge variant="outline" class="flex items-center gap-1">
                      <Users class="h-3 w-3" />
                      {{ sub.students }}
                    </Badge>
                  </TableCell>

                  <!-- Actions -->
                  <TableCell class="text-right">
                    <Button variant="ghost" size="icon">
                      <MoreHorizontal class="h-4 w-4" />
                    </Button>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>

      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
